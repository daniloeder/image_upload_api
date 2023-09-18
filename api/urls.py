from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ImageViewSet, TierViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'images', ImageViewSet)
router.register(r'tiers', TierViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
