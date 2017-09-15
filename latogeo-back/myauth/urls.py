from . import views
from django.conf.urls import patterns, include, url
from account.views import (createOrLogin, myLogout, MyRecover, MyRecoverDone,
                            MyReset, MyResetDone, accountSettings,
                            updateUserInfo, paymentProcessing)

urlpatterns = [
    url(r'^validar_email/(?P<id>[0-9]+)/(?P<hash>[^/]+)$', views.validate_email,
        name='validate_email'),
    url(r'^enviar_confirmacao/$', views.send_confirmation,
        name='send_confirmation'),
    url(r'^$', createOrLogin, name='create_or_login'),
    url(r'^logout/$', myLogout, name='logout'),
    url(r'^ajustes/$', accountSettings, name='account_settings'),
    url(r'^update_user/$', updateUserInfo, name='update_user'),
    url(r'^recover/$', MyRecover.as_view(), name='my_recover'),
    url(r'^recover/(?P<signature>.+)/$',
		MyRecoverDone.as_view(),
		name='my_recover_done'),
    url(r'^reset/(?P<token>[\w:-]+)/$',
		MyReset.as_view(),
		name='my_reset'),
    url(r'^reset/done$', MyResetDone.as_view(), name='my_reset_done'),
]

