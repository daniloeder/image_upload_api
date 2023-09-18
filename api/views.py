from rest_framework import viewsets
from .models import Image, Tier
from .serializers import ImageSerializer, TierSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class TierViewSet(viewsets.ModelViewSet):
    queryset = Tier.objects.all()
    serializer_class = TierSerializer
