from loan.models import Loan
from .serializers import LoanPostSerializer, LoanGetSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import (
        SessionAuthentication, BasicAuthentication, TokenAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import mixins


class LoanViewSet(  mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    authentication_classes = (SessionAuthentication, TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = LoanPostSerializer
    queryset = Loan.objects.all()
    #filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    #filter_fields = ('id','student__email',)
    #search_fields = ('patrimony','spec__name', 'spec__kind__name')

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return LoanPostSerializer
        return LoanGetSerializer

    def get_queryset(self):
        return self.request.user.loan_student.all()

    def create(self, request, *args, **kwargs):
        print(request.user.id)
        request.data['student'] = request.user.id
        print(request.data)
        return super(self.__class__, self).create(request, *args, **kwargs)

    @detail_route(methods=['patch'])
    def cancel(self, request, pk=None):
        instance = self.get_object()
        instance.status = Loan.CANCELED
        serializer = LoanPostSerializer(
                instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

