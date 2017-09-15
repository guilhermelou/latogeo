# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import Http404
from myauth.models import MyUser
from django.contrib import messages
from django.http import (HttpResponse, HttpResponseRedirect)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from password_reset.views import (Recover, RecoverDone, Reset, ResetDone)
from password_reset.utils import get_username
from django.template import loader
from django.core.mail import send_mail
from django.conf import settings
from django.core import signing
from django.forms.models import model_to_dict
from myauth.models import MyUser
import json
from django.core import serializers
from myauth.forms import (UserCreationForm, PubUserChangeForm, UserChangeForm,
                            AddressChangeForm)

# Create your views here.

def validate_email(request, id, hash):
    """View to verify the user's hash and confirm his email account.
    If its all ok the view redirects to logged home page, if not redirects to
    send confirmation page
    """
    try:
        user = MyUser.objects.get(id=id)
        if (user.confirm_email(hash)):
            user = authenticate(id=id, hash=hash)
            login(request,user)
            return redirect('home:home')
        else:
            return redirect('myauth:send_confirmation')
    except:
        return redirect('myauth:send_confirmation')

def send_confirmation(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            user = MyUser.objects.get(email=email)
            user.send_confirmation()
            messages.success(request, u'Email de confirmação enviado com \
                                        sucesso!')
        except:
            messages.warning(request, u'Email não cadastrado no sistema!')
            email = None
    else:
        try:
            email = request.GET['email']
        except:
            email = None

    return render(request, 'myauth/send_confirmation.html',
            {
                'email': email,
            }
    )

#function to create user, if creation is ok return true, if not return the form
def createUser(request):
    # checking form, if valid login, if not redirect to home
    form = UserCreationForm(data=request.POST)
    if form.is_valid():
        user = form.save()
        user.send_confirmation()
        return True
    else:
        return form


#function to login, if login is ok return true, if not return the form
def myLogin(request):
    '''This function is made to login a user from form, user only be allowed to
    login if email is validated
    '''
    # checking form, if valid login, if not redirect to home
    form = AuthenticationForm(data=request.POST)
    print form.data
    # Important! The user will only be allowed to login if email
    # is confirmed
    if form.is_valid() and form.get_user().is_confirmed:
        # user = form.save()
        login(request, form.get_user())
        if not request.POST.get('remember', None):
            print 'not remember'
            request.session.set_expiry(0)
        return True
    else:
        return form


#view to handle the auth way, creation or authentication
def createOrLogin(request):
    # if next uses him, if not uses /. If user is already authenticated
    # redirect
    try:
        next = request.GET['next']
    except:
        next = "/home/"
    # redirects user to other page if authenticated
    if request.user.is_authenticated():
        return HttpResponseRedirect(next)
    # setting tab to show
    is_login = True
    # checking post or get
    if request.method == 'POST':
        if 'logging' in request.POST:
            creation_form = UserCreationForm()
            login_form = myLogin(request)
            if login_form == True:
                return HttpResponseRedirect(next)
        elif 'creating' in request.POST:
            is_login=False
            login_form = AuthenticationForm()
            creation_form = createUser(request)
            if creation_form == True:
                messages.success(
                    request,
                    u'Email de confirmação enviado com sucesso!'
                )
                return HttpResponseRedirect(
                    reverse_lazy(
                        'myauth:send_confirmation'
                    )
                )
    else:
        login_form = AuthenticationForm()
        creation_form = UserCreationForm()
    return render(request, 'account/account.html',
        {
            'login_form': login_form,
            'creation_form': creation_form,
            'next': next,
            'is_login': is_login
        }
    )


@login_required
def accountSettings(request):
    """View to the user change his own info
    """
    # Change only by post
    if request.method == 'POST':
        # Checking if the user is requesting the user_change_form
        if 'user_change' in request.POST:
            # loading the password form to a future request
            password_form = PasswordChangeForm(
                user=request.user,
                prefix='password_form'
            )
            # loading the user_change_form with the data on POST
            user_change_form = PubUserChangeForm(
                    request.POST, instance=request.user)
            # if valids the form will be saved and send a success message
            if user_change_form .is_valid():
                user_changed = user_change_form.save()
                messages.success(request, u'Usuário alterado com sucesso!')
            else:
                messages.warning(request, u'Houve um problema em alterar \
                                 seus dados de usuário')
        # Checking if the user is requesting to change his password
        elif 'password' in request.POST:
            # loading the user_change_form to a future request
            user_change_form = PubUserChangeForm(instance=request.user)
            # loading the password_form with the data on POST
            password_form = PasswordChangeForm(
                user=request.user,
                data = request.POST,
                prefix='password_form'
                )
            # if password valids form will be saved and send a success
            # message
            if password_form.is_valid():
                user = password_form.save()
                messages.success(request, u'Senha atualizada com sucesso!')
            else:
                messages.warning(request, u'Houve um problema em alterar \
                                 sua senha')
        # Checking if the user is requesting to change his establishment
        # address
        elif 'address_change' in request.POST:
            # loading both forms to future requests
            password_form = PasswordChangeForm(
                user=request.user,
                prefix='password_form'
            )
            user_change_form = PubUserChangeForm(instance=request.user)
            # try to get post values passed by jquery
            try:
                address = request.POST['address']
                lat = request.POST['lat']
                long = request.POST['long']
                # updating user address
                request.user.address = address
                request.user.lat = lat
                request.user.long = long
                # saving user new info
                request.user.save()
                return HttpResponse("1", content_type="text/json")
                # messages.success(request, u'Endereço alterado com sucesso!')
            except:
                return HttpResponse("0", content_type="text/json")
                # messages.warning(request, u'Houve um problema em alterar seu \
                #                    endereço, para qualquer dúvida entre em \
                #                    contato conosco')
        else:
            # loading both forms to future requests
            password_form = PasswordChangeForm(
                user=request.user,
                prefix='password_form'
            )
            user_change_form = PubUserChangeForm(instance=request.user)
            # user is singing the plan
            if 'sign_plan' in request.POST:
                request.user.payment_status = request.user.AWATING_APPROVAL
                messages.success(request, u'Requisição de assinatura enviada \
                                 com sucesso, aguarde a aprovação no seu \
                                 email!')
            # user is canceling the plan
            elif 'cancel_plan' in request.POST:
                request.user.payment_status = request.user.FREE_TRY
                messages.success(request, u'Assinatura cancelada com sucesso!')
    else:
        password_form = PasswordChangeForm(
            user=request.user,
            prefix='password_form'
        )
        user_change_form = PubUserChangeForm(instance=request.user)

    # return the request values into the template
    return render(request, 'account/account_settings.html',
            {   'password_form': password_form,
                'user_change_form': user_change_form
            }
    )


# simple view to make logout
def myLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('index'))

def updateUserInfo(request):
    user_dict = {"user": 0}
    user_json = {}
    if request.user.is_anonymous():
        user_json = json.dumps(user_dict)
    else:
        try:
            serialized_object = serializers.serialize('json', [request.user,])
            user_dict = json.loads(serialized_object)
            user_json = json.dumps({"user": user_dict[0]})
        except:
            user_json = json.dumps({"user": 0})
    return HttpResponse(user_json, content_type='application/json')

# This classes follows the documentation and nomination of the files of this
# link http://django-password-reset.readthedocs.io/en/latest/views.html

class MyRecover(Recover):
    template_name = "account/recovery_form.html"
    search_fields = ['email']
    success_url_name = 'account:my_recover_done'
    email_template_name = 'account/recovery_email.txt'
    email_subject_template_name = 'account/recovery_email_subject.txt'
    def send_notification(self):
        context = {
            'site': self.get_site(),
            'user': self.user,
            'username': get_username(self.user),
            'token': signing.dumps(self.user.pk, salt=self.salt),
            'secure': self.request.is_secure(),
        }
        body = loader.render_to_string(self.email_template_name,
                                                context).strip()
        subject = loader.render_to_string(self.email_subject_template_name,
                                                context).strip()
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL,
                                                [self.user.email],
                                                html_message=body)

class MyRecoverDone(RecoverDone):
    template_name = "account/reset_sent.html"


class MyReset(Reset):
    template_name = "account/reset.html"
    success_url = reverse_lazy("account:my_reset_done")


class MyResetDone(ResetDone):
    template_name = "account/recovery_done.html"

