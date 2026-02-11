from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Account

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