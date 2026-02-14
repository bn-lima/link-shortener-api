from django.urls import include, path
from .views import UrlShortener, RedirectToOriginalUrl

urlpatterns = [
    path('', include([
        path('url/', UrlShortener.as_view(), name='url'),
        path('<str:link_id>/', RedirectToOriginalUrl.as_view(), name='redirect')
    ]))
]