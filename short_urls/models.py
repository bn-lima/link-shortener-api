from django.db import models
from .services import  create_formated_uuid, get_short_url

class ShortUrls(models.Model):
    original_url = models.URLField(max_length=5000)
    id_token = models.CharField(max_length=9, default=create_formated_uuid, unique=True)
    short_url = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = get_short_url(self.id_token)
        return super().save(*args, **kwargs)