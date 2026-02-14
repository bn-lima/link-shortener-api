from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import UrlShortenerSerializer, RedirectToOriginalUrlSerialzer
from rest_framework.response import Response

class UrlShortener(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = UrlShortenerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        url = serializer.save()

        return Response({"short_url": url.short_url})
    
class RedirectToOriginalUrl(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, link_id, *args, **kwargs):
        serializer = RedirectToOriginalUrlSerialzer(data={}, context={"link_id": link_id})
        serializer.is_valid(raise_exception=True)
        short_link = serializer.save()

        return redirect(short_link.original_url)