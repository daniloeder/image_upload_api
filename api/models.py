from django.contrib.auth.models import User
from django.db import models

class Tier(models.Model):
    name = models.CharField(max_length=100)
    thumbnail_sizes = models.BooleanField(help_text="Allow arbitrary thumbnail sizes")
    allow_original_link = models.BooleanField(help_text="Allow presence of the link to the originally uploaded file")
    allow_expiring_link = models.BooleanField(help_text="Allow ability to generate expiring links")

    def __str__(self):
        return self.name


def get_tiers():
    """Returns a list of all tiers."""
    tiers = Tier.objects.all()
    return tiers


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    expiring_link_seconds = models.PositiveIntegerField(null=True, blank=True, help_text="Expiring link duration in seconds (between 300 and 30000)")

    TIER_CHOICES = [
        (tier.name, tier.name) for tier in get_tiers()
    ]

    tier = models.CharField(max_length=20, choices=TIER_CHOICES)

    def generate_links(self):
        """Generates and sets the basic_link, premium_link, original_link, and expiring_link fields according to the user tier."""
        
        self.link_200px = self.generate_basic_link()

        if self.tier == 'Premium':
            self.link_400px = self.generate_premium_link()
        elif self.tier == 'Enterprise':
            self.link_400px = self.generate_premium_link()

        if self.tier.allow_original_link:
            self.original_link = self.generate_original_link()

        if self.tier.allow_expiring_link:
            self.expiring_link = self.generate_expiring_link()

        self.save()

    def generate_basic_link(self):
        """Generates a link to a thumbnail that is 200px in height."""
        thumbnail_url = "http://localhost:8000/api/images/thumbnails/basic_{}_{}".format(200, self.image.name)
        return thumbnail_url

    def generate_premium_link(self):
        """Generates a link to a thumbnail that is 200px in height and a link to a thumbnail that is 400px in height."""
        thumbnail_400px_url = "http://localhost:8000/api/images/thumbnails/basic_{}_{}".format(400, self.image.name)
        return thumbnail_400px_url

    def generate_original_link(self):
        """Generates a link to the originally uploaded image."""
        original_link = "http://localhost:8000/api/images/uploads/{}".format(self.image.name)
        return original_link

    def generate_expiring_link(self):
        """Generates an expiring link to the image. The link expires after a given number of seconds, which can be specified by the user."""
        expiring_link = "http://localhost:8000/api/images/expiring/{}/{}".format(self.image.name, self.expiring_link_seconds)
        return expiring_link