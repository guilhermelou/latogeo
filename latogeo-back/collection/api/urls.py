from django.conf.urls import url

from collection.api.views import (
        ItemKindViewSet,
        ItemSpecViewSet,
        ItemViewSet
        )
from rest_framework.routers import DefaultRouter, SimpleRouter

router = SimpleRouter()
router.register(r'items/kinds', ItemKindViewSet)
router.register(r'items/specs', ItemSpecViewSet)
router.register(r'items', ItemViewSet)

# urlpatterns += router.urls

