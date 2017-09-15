"""latogeo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from patches import routers

from collection.api.urls import router as collection_router
from myauth.api.urls import router as myauth_router
from college.api.urls import router as college_router
from loan.api.urls import router as loan_router
from rest_framework.authtoken import views


router = routers.DefaultRouter()
router.extend(collection_router)
router.extend(myauth_router)
router.extend(college_router)
router.extend(loan_router)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^acervo/', include('collection.urls', namespace='collection')),
    url(r'^recuperar_senha/', include('password_reset.urls')),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls, namespace='api')),
]
