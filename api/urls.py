from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImageViewSet, TierViewSet

router = DefaultRouter()
router.register(r'images', ImageViewSet)
router.register(r'tiers', TierViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
