from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import ImageViewSet, TierViewSet, ImageUploadView

router = DefaultRouter()
router.register(r'images', ImageViewSet)
router.register(r'tiers', TierViewSet)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('images/list/', ImageViewSet.as_view({'get': 'list'}), name='image-list'),
    path('images/upload/', ImageUploadView.as_view(), name='image-upload'),
    path('', include(router.urls)),
]