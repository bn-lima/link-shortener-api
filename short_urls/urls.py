from django.urls import include, path
from .views import UrlShortener

urlpatterns = [
    path('', include([
        path('url/', UrlShortener.as_view(), name='url')
    ]))
]