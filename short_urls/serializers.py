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
    
class RedirectToOriginalUrlSerialzer(serializers.Serializer):
    
    def validate(self, data):
        link_id = self.context.get("link_id")

        try:
            short_obj = ShortUrls.objects.get(id_token=link_id)
        except ShortUrls.DoesNotExist:
            raise serializers.ValidationError("Invalid link id")

        data['short_obj'] = short_obj
        return data
    
    def save(self, **kwargs):
        return self.validated_data.get("short_obj")