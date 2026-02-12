from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timedelta
from django.utils import timezone
import uuid

class Account(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    def __str__(self):
        return f'{self.username}'

class ResetToken(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='reset_tokens')
    key = models.UUIDField(default=uuid.uuid4)
    expiration = models.DateTimeField()
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):

        if not self.expiration:
            self.expiration = timezone.now() + timedelta(hours=1)

        return super().save(*args, **kwargs)
    
    def is_expired(self, *args, **kwargs):
        return timezone.now() >= self.expiration
    
    def desactive(self, *args, **kwargs):
        self.active = False
        self.save()