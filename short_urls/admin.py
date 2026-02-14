from django.contrib import admin
from .models import ShortUrls

@admin.register(ShortUrls)
class ShortUrlsAdmin(admin.ModelAdmin):
    list_display = ['original_url', 'id_token', 'short_url']
    search_fields = ['original_url', 'id_token', 'short_url']
