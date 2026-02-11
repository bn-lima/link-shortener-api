from django.urls import path, include
from .views import Register, Logout, Login

urlpatterns = [
    path('', include([
        path('register/', Register.as_view(), name='register'),
        path('logout/', Logout.as_view(), name='logout'),
        path('login/', Login.as_view(), name='login')
    ]))
]