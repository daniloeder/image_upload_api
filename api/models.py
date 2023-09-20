from django.contrib.auth.models import User
from django.db import models

class Tier(models.Model):
    name = models.CharField(max_length=100)
    thumbnail_sizes = models.CharField(max_length=255, help_text="Comma-separated list of thumbnail sizes (e.g., '200x200,400x400')")
    allow_original_link = models.BooleanField()
    allow_expiring_link = models.BooleanField()

    def __str__(self):
        return self.name

class CustomTier(models.Model):
    name = models.CharField(max_length=100)
    thumbnail_sizes = models.CharField(max_length=255, help_text="Comma-separated list of thumbnail sizes (e.g., '200x200,400x400')")
    allow_original_link = models.BooleanField()
    allow_expiring_link = models.BooleanField()
    expiring_link_seconds = models.PositiveIntegerField(help_text="Expiring link duration in seconds (between 300 and 30000)")

    def __str__(self):
        return self.name

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    TIER_CHOICES = [
        ('Basic', 'Basic'),
        ('Premium', 'Premium'),
        ('Enterprise', 'Enterprise'),
    ]

    tier = models.CharField(max_length=20, choices=TIER_CHOICES)
    expiring_link_seconds = models.PositiveIntegerField(null=True, blank=True, help_text="Expiring link duration in seconds (between 300 and 30000)")

    def generate_links(self):
        if self.tier == 'Basic':
            self.basic_link = self.generate_basic_link()
        elif self.tier == 'Premium':
            self.basic_link = self.generate_basic_link()
            self.premium_link = self.generate_premium_link()
            self.original_link = self.generate_original_link()
        elif self.tier == 'Enterprise':
            self.basic_link = self.generate_basic_link()
            self.premium_link = self.generate_premium_link()
            self.original_link = self.generate_original_link()
            self.expiring_link_seconds = self.generate_expiring_link_seconds()

        self.save()

    def generate_basic_link(self):
        # Generate and return the basic link
        return "Basic Link Here"

    def generate_premium_link(self):
        # Generate and return the premium link
        return "Premium Link Here"

    def generate_original_link(self):
        # Generate and return the original link
        return "Original Link Here"

    def generate_expiring_link_seconds(self):
        # Generate and return the expiring link seconds
        return 3600
