from college.models import Course, Discipline
from college.api.serializers import CourseSerializer, DisciplineGetSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import (
        SessionAuthentication, BasicAuthentication, TokenAuthentication)
from rest_framework.permissions import IsAuthenticated



class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    authentication_classes = (SessionAuthentication, TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = (
            'name','cod', 'course_discipline__name', 'course_discipline__cod')

class DisciplineViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    authentication_classes = (SessionAuthentication, TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = DisciplineGetSerializer
    queryset = Discipline.objects.all()

