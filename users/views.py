from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import RegisterSerializer, LoginSerializer, ChangePasswordRequestSerializer, ChangePasswordSerializer
from rest_framework.response import Response
from rest_framework import status
from .auth_services import logout_user, get_and_validate_reset_token

class Register(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):

        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = serializer.save()

        return Response({'auth_token': token.key}, status=status.HTTP_201_CREATED)
    
class Logout(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user
        logout_user(user)

        return Response({'detail': 'Logout successful'}, status=status.HTTP_204_NO_CONTENT)
    
class Login(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        token = serializer.save()

        if not token:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"auth_token": token.key})
    
class ChangePasswordRequest(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user

        serializer = ChangePasswordRequestSerializer(data={}, context={"user":user})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"detail": "An email with a reset token has been sent to you."}, status=status.HTTP_200_OK)
    
class ChangePassword(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        user = request.user

        str_token = request.query_params.get("reset_token")

        if not str_token:
            return Response({"detail": "Reset token is required."}, status=status.HTTP_400_BAD_REQUEST)

        token = get_and_validate_reset_token(str_token)

        if not token:
            return Response({"detail": "Invalid or inactive reset token"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = ChangePasswordSerializer(data=request.data, context={'user':user})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"detail": "Your password has been changed successfully."})
        