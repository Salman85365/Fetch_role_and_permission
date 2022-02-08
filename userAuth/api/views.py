from ..common import BaseAPIView,validation_error_response,success_response
from .serializers import AuthUserSerializer
from rest_framework.permissions import AllowAny
from ..models import User
from rest_framework import generics
from django.contrib import auth



from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer

class AuthUser(BaseAPIView):
    serializer_class = AuthUserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *a, **kw):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                user_obj = User.objects.get(username=serializer.data['username'])
            except User.DoesNotExist:
                return Response(validation_error_response("User not existed"))
            result = user_obj.check_password(serializer.data['password'])
            if not result:
                return Response(validation_error_response("Invalid Password"))
            auth.authenticate(user_obj)
            data = {
                "username":user_obj.username,
                "user_role":user_obj.role,
                "permission":list(user_obj.user_permissions.values_list("name",flat=True))
            }
            return Response(success_response(data))
        else:
            return Response(validation_error_response(serializer.errors))


# Register API
from django.contrib.auth import get_user_model

User = get_user_model()
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })