from django.db import models
from .services import get_url_domain, create_formated_uuid
import uuid

class ShortUrls(models.Model):
    original_url = models.URLField(max_length=600)
    id_token = models.CharField(max_length=9, default=create_formated_uuid)
    short_url = models.SlugField(max_length=50) #Verificar se pode blank=false

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = get_url_domain(self.original_url) + self.id_token
        return super().save(*args, **kwargs)
