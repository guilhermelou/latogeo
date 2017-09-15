from rest_framework.generics import ListAPIView
from collection.models import Item, ItemKind, ItemSpec
from .serializers import (ItemKindSerializer, ItemSpecSerializer,
        ItemSerializer, ItemGetSerializer)
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import (
        SessionAuthentication, BasicAuthentication, TokenAuthentication)
from rest_framework.permissions import IsAuthenticated


class ItemKindViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    authentication_classes = (SessionAuthentication, TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ItemKindSerializer
    queryset = ItemKind.objects.all()
    # filter_backends = (filters.SearchFilter,)
    # filter_fields = ('id',)
    # search_fields = (
    #        'spec_kind__name','name', 'spec_kind__item_spec__patrimony',)

class ItemSpecViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ItemSpecSerializer
    queryset = ItemSpec.objects.all()

class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    authentication_classes = (SessionAuthentication, TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ItemGetSerializer
    queryset = Item.objects.all()
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    filter_fields = ('id',)
    search_fields = ('patrimony','spec__name', 'spec__kind__name')

