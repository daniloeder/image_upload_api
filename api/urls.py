from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import ImageViewSet, TierViewSet, CustomTierViewSet
from .models import CustomTier

router = DefaultRouter()
router.register(r'images', ImageViewSet)
router.register(r'tiers', TierViewSet)
router.register(r'custom-tiers', CustomTierViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

