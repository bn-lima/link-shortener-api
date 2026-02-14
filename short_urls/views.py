from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import UrlShortenerSerializer
from rest_framework.response import Response

class UrlShortener(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = UrlShortenerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        url = serializer.save()

        return Response({"short_url": url.short_url})
