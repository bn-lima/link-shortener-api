from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import ResetToken
import uuid

def logout_user(user):
    token = Token.objects.get(user=user)
    token.delete()

def authenticate_user(email, password):
    user = authenticate(username=email, password=password)

    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return token
    return None

def desactive_reset_tokens(user):
    for token in user.reset_tokens.all():
        if token.active:
            token.active = False
            token.save()

def has_many_reset_tokens(user):

    if user.reset_tokens.filter(active=True).count() >= 3:
        return True
    return False

def get_and_validate_reset_token(str_token):

    try:
        uuid_token = uuid.UUID(str_token)
    except ValueError:
        return None
    
    try:
        token = ResetToken.objects.get(key=uuid_token)
    except ResetToken.DoesNotExist:
        return None
    
    if not token.active:
        return None
    return token