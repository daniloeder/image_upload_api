from django.contrib import admin
from .models import Image, Tier

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'uploaded_at', 'tier', 'expiring_link_seconds')
    list_filter = ('tier',)
    search_fields = ('user__username', 'image')
    date_hierarchy = 'uploaded_at'

@admin.register(Tier)
class TierAdmin(admin.ModelAdmin):
    list_display = ('name', 'allow_original_link', 'allow_expiring_link')
