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

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.save(user=request.user)

            # Generate links based on user's tier
            image.generate_links()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
