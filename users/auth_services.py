from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

def logout_user(user):
    token = Token.objects.get(user=user)
    token.delete()

def authenticate_user(email, password):
    user = authenticate(username=email, password=password)

    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return token
    return None