from rest_framework import serializers
from .models import Image, Tier

class ImageSerializer(serializers.ModelSerializer):
    link_200px = serializers.CharField(max_length=255, read_only=True)
    link_400px = serializers.CharField(max_length=255, read_only=True)
    original_link = serializers.CharField(max_length=255, read_only=True)
    expiring_link = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Image
        fields = '__all__'

    def to_representation(self, instance):
        """Serializes the Image object."""
        data = super().to_representation(instance)

        links = instance.generate_links()
        if links is None:
            return data

        data.update(links)

        return data


class TierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tier
        fields = '__all__'