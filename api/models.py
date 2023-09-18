from django.db import models
from django.contrib.auth.models import User as DjangoUser

class Tier(models.Model):
    name = models.CharField(max_length=100)
    thumbnail_sizes = models.JSONField()
    allow_original_link = models.BooleanField()
    allow_expiring_link = models.BooleanField()
    
    def __str__(self):
        return self.name

class Image(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    tier = models.ForeignKey(Tier, on_delete=models.PROTECT)
    expiring_link_seconds = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"Image by {self.user.username} uploaded at {self.uploaded_at}"

