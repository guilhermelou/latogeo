# -*- coding: utf-8 -*-
import warnings
from django.core.exceptions import ImproperlyConfigured
from django.core.mail import send_mail
from django.db import models, migrations
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,\
    BaseUserManager
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
import time
import hashlib
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context, loader
from django.conf import settings
import uuid


class MyUserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError(_('The given email must be set'))
        if not password:
            raise ValueError(_('The given password must be set'))
        email = MyUserManager.normalize_email(email)
        user = self.model(
                email=email,
                is_staff=False, is_active=True, is_superuser=False,
                last_login=now, date_joined=now,
                **extra_fields
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        u = self.create_user(email, password, **extra_fields)
        u.is_staff = True
        u.is_active = True
        u.is_superuser = True
        u.save(using=self._db)
        return u


class MyUser(AbstractBaseUser, PermissionsMixin):
    STUDENT = 0
    OFFICER = 1
    PROFESSOR = 2
    CHIEF = 3
    LEVEL = (
        (STUDENT, _('Student')),
        (OFFICER, _('Officer')),
        (PROFESSOR, _('Professor')),
        (CHIEF, _('Chief')),
    )
    # Level of the user Student = 0, Officer = 1, Professor = 2
    level = models.SmallIntegerField(_('Level'), default=0, choices=LEVEL)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    ra = models.CharField(_('RA'), max_length=30, blank=True, null=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    terms = models.BooleanField(_('Terms'), default=False,
        help_text=_('Designates if the user accepted the terms of use'))
    confirmation_key = models.UUIDField(u'Chave de Confirmação', unique=True,
                                        default=uuid.uuid4)
    is_confirmed = models.BooleanField('Email Confirmado', default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def confirmation_key_str(self):
        "Returns the confirmation key as string"
        return str(self.confirmation_key)

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

    def send_confirmation(self):
        """
        Sends a email confirmation with the key
        """
        plaintext = get_template('myauth/email_confirmation.txt')
        html     = get_template('myauth/email_confirmation.html')

        d = Context({ 'user': self })
        text_content = plaintext.render(d)
        html_content = html.render(d)

        subject = u'Confirmação de Email'
        from_email, to = settings.EMAIL_HOST_USER, self.email

        msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
        msg.content_subtype = "html"
        msg.send()
        '''
        text_template = 'myauth/email_confirmation.txt'
        html_template = 'myauth/email_confirmation.html'

        body = loader.render_to_string(
            html_template,
            {'user': self}
        ).strip()
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL,
                                                [self.email],
                                                html_message=body)
        '''

    def confirm_email(self, hash):
        """
        Check the key and, if equals change the boolean 'is_confirmed' to True
        and return True. if not does nothing and return False
        """
        if self.confirmation_key_str() == hash:
            self.is_confirmed = True
            self.save()
            return True
        else:
            return False

    class Meta:
        verbose_name = (u'Usuário')
        verbose_name_plural = (u'Usuários')

