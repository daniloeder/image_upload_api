from django.contrib.auth.models import User
from django.db import models

class Tier(models.Model):
    # Fields for the Tier model
    name = models.CharField(max_length=100)
    thumbnail_sizes = models.CharField(max_length=255, help_text="Comma-separated list of thumbnail sizes (e.g., '200x200,400x400')")
    allow_original_link = models.BooleanField()
    allow_expiring_link = models.BooleanField()

    # String representation of Tier
    def __str__(self):
        return self.name

class Image(models.Model):
    # Fields for the Image model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    tier = models.ForeignKey(Tier, on_delete=models.PROTECT)
    expiring_link_seconds = models.PositiveIntegerField(null=True, blank=True, help_text="Expiring link duration in seconds (between 300 and 30000)")

    # String representation of Image
    def __str__(self):
        return f"Image by {self.user.username} uploaded at {self.uploaded_at}"

class CustomTier(models.Model):
    # Fields for the CustomTier model
    name = models.CharField(max_length=100)
    allow_original_link = models.BooleanField(default=False)
    allow_expiring_link = models.BooleanField(default=False)
    thumbnail_sizes = models.CharField(max_length=255, help_text="Comma-separated list of thumbnail sizes (e.g., '200x200,400x400')")
    expiring_link_seconds = models.PositiveIntegerField(help_text="Expiring link duration in seconds (between 300 and 30000)")

    # String representation of CustomTier
    def __str__(self):
        return self.name
