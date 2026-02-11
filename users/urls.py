from django.urls import path, include
from .views import Register, Logout

urlpatterns = [
    path('', include([
        path('register/', Register.as_view(), name='register'),
        path('logout/', Logout.as_view(), name='logout'),
    ]))
]