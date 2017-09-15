from django.conf.urls import url

from college.api.views import (
        CourseViewSet,
        DisciplineViewSet
        )
from rest_framework.routers import DefaultRouter, SimpleRouter

router = SimpleRouter()
router.register(r'courses', CourseViewSet)
router.register(r'disciplines', DisciplineViewSet)


