from rest_framework.generics import ListAPIView
from myauth.models import MyUser
from myauth.api.serializers import MyUserSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import (
        SessionAuthentication, BasicAuthentication, TokenAuthentication)
from rest_framework.permissions import IsAuthenticated



class MyUserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    authentication_classes = (SessionAuthentication, TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = MyUserSerializer
    queryset = MyUser.objects.all()
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ('first_name','last_name', 'email', 'ra')


class StudentViewSet(MyUserViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = MyUser.objects.filter(level__lt=1)

class ProfessorOrChiefViewSet(MyUserViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = MyUser.objects.filter(level__gt=1)

