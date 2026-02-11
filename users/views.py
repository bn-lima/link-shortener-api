from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from .auth_services import logout_user

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