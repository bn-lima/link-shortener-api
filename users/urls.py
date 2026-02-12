from django.urls import path, include
from .views import Register, Logout, Login, ChangePasswordRequest, ChangePassword

urlpatterns = [
    path('', include([
        path('register/', Register.as_view(), name='register'),
        path('logout/', Logout.as_view(), name='logout'),
        path('login/', Login.as_view(), name='login'),

        path('password/', include([
            path('change/', include([
                path('', ChangePassword.as_view(), name='change'),
                path('request/', ChangePasswordRequest.as_view(), name='request')
            ]))
        ]))
    ]))
]