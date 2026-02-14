from rest_framework import serializers
from .models import ShortUrls

class UrlShortenerSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShortUrls
        fields = '__all__'
        read_only_fields = ('id_token', 'short_url')

    def create(self, validated_data):
        original_url = validated_data.get('original_url')

        shorturl_obj = ShortUrls.objects.create(
            original_url=original_url
        )

        return shorturl_obj