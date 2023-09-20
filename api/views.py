from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .models import Image, Tier, CustomTier
from .serializers import ImageSerializer, TierSerializer, CustomTierSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class TierViewSet(viewsets.ModelViewSet):
    queryset = Tier.objects.all()
    serializer_class = TierSerializer

class CustomTierViewSet(viewsets.ModelViewSet):
    queryset = CustomTier.objects.all()
    serializer_class = CustomTierSerializer