from django.conf.urls import url

from myauth.api.views import (
        MyUserViewSet,
        StudentViewSet,
        ProfessorOrChiefViewSet
        )
from rest_framework.routers import DefaultRouter, SimpleRouter

router = SimpleRouter()
router.register(r'users/professors_or_chiefs', ProfessorOrChiefViewSet)
router.register(r'users/students', StudentViewSet)
router.register(r'users', MyUserViewSet)

