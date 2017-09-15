from django.conf.urls import url

from loan.api.views import (
        LoanViewSet
        )
from rest_framework.routers import DefaultRouter, SimpleRouter

router = SimpleRouter()
router.register(r'loans', LoanViewSet)

