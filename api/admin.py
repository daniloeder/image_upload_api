from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User as DjangoUser
from .models import Image, Tier, CustomTier  # Import CustomTier

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

# Register your custom UserAdmin class for the User model
admin.site.unregister(DjangoUser)  # Unregister the default UserAdmin
admin.site.register(DjangoUser, CustomUserAdmin)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'uploaded_at', 'tier', 'expiring_link_seconds')
    list_filter = ('tier',)
    search_fields = ('user__username', 'image')
    date_hierarchy = 'uploaded_at'

@admin.register(Tier)
class TierAdmin(admin.ModelAdmin):
    list_display = ('name', 'allow_original_link', 'allow_expiring_link')

@admin.register(CustomTier)  # Register the CustomTier model
class CustomTierAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail_sizes', 'allow_original_link', 'allow_expiring_link', 'expiring_link_seconds')
