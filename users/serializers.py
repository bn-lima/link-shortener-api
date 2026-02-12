from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Account, ResetToken
from .auth_services import authenticate_user, has_many_reset_tokens, desactive_reset_tokens, logout_user
from .email import send_reset_token_by_email
class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=128, required=True)

    class Meta:
        model = Account
        fields = ('username', 'email', 'password', 'confirm_password')

    def validate(self, data):
        password = data['password']
        confirm_password = data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError('Passwords do not match')
        
        return data
    
    def save(self, **kwargs):
        self.validated_data.pop('confirm_password')
        password = self.validated_data.pop('password')

        
        user = Account.objects.create(**self.validated_data)
        user.set_password(password)
        user.save()

        token =Token.objects.create(user=user)

        return token
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=150)
    password = serializers.CharField(max_length=128)

    def validate(self, data):
        email = data['email']
        password = data['password']

        token = authenticate_user(email, password)

        if token:
            data['token'] = token
        return data
    
    def save(self, **kwargs):
        try:
            token = self.validated_data.get('token')
        except Exception:

            return None
        return token
    
class ChangePasswordRequestSerializer(serializers.Serializer):
    
    def validate(self, data):
        user = self.context.get('user')

        if has_many_reset_tokens(user):
            raise serializers.ValidationError({"detail": "You have too many active reset tokens. Reset your password by clicking the link sent to your email, or please wait one hour."})
        
        return data
    
    def save(self, **kwargs):
        user = self.context.get('user')

        token = ResetToken.objects.create(user=user)    
        send_reset_token_by_email(user.email, token.key)

class ChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(max_length=128, required=True)
    confirm_password = serializers.CharField(max_length=128, required=True)

    def validate(self, data):
        user = self.context.get("user")
        new_password = data["new_password"]
        confirm_password = data["confirm_password"]

        if user.check_password(new_password):
            raise serializers.ValidationError({"detail": "The new password cannot be the same as your current password."})
        
        if new_password != confirm_password:
            raise serializers.ValidationError("The passwords do not match")
        
        return data
        
    def save(self, **kwargs):
        user = self.context.get('user')
        new_password = self.validated_data.get('new_password')

        user.set_password(new_password)
        user.save()

        desactive_reset_tokens(user)
        logout_user(user)