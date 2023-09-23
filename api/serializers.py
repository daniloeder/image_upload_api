from rest_framework import serializers
from .models import Image, Tier, CustomTier

class ImageSerializer(serializers.ModelSerializer):
    basic_link = serializers.CharField(max_length=255, read_only=True)
    premium_link = serializers.CharField(max_length=255, read_only=True)
    original_link = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Image
        fields = '__all__'

    def to_representation(self, instance):
        """Generates the basic_link, premium_link, and original_link fields according to the user tier."""
        data = super().to_representation(instance)

        if instance.tier == 'Basic':
            data['basic_link'] = instance.generate_basic_link()
        elif instance.tier == 'Premium':
            data['basic_link'] = instance.generate_basic_link()
            data['premium_link'] = instance.generate_premium_link()
            data['original_link'] = instance.generate_original_link()
        elif instance.tier == 'Enterprise':
            data['basic_link'] = instance.generate_basic_link()
            data['premium_link'] = instance.generate_premium_link()
            data['original_link'] = instance.generate_original_link()

        return data

class TierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tier
        fields = '__all__'

class CustomTierSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomTier
        fields = '__all__'