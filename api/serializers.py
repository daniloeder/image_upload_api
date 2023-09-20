from rest_framework import serializers
from .models import Image, Tier, CustomTier

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class TierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tier
        fields = '__all__'

class CustomTierSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomTier
        fields = '__all__'
