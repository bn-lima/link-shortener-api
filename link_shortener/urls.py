from django.contrib import admin
from django.urls import path, include   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('users.urls')),
    path('short/', include('short_urls.urls'))
]
