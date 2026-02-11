from rest_framework.authtoken.models import Token

def logout_user(user):
    token = Token.objects.get(user=user)
    token.delete()