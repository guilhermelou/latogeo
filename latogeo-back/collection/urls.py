from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^emprestimo/$', views.LoanView.as_view(), name='loan')
]
