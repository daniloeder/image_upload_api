from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .models import Image, Tier
from .serializers import ImageSerializer, TierSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def retrieve(self, request, pk=None):
        image = super().retrieve(request, pk).data

        if image['tier'] == 'Enterprise':
            image['expiring_link'] = self.generate_expiring_link(image['id'])

        return Response(image)

    def generate_expiring_link(self, image_id):
        url = generate_presigned_url(image_id)
        url.expires_in = image['expiring_link_seconds']

        return url

class TierViewSet(viewsets.ModelViewSet):
    queryset = Tier.objects.all()
    serializer_class = TierSerializer

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.save(user=request.user)
            image.generate_links()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
