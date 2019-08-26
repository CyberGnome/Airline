from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from users.api.register.serializers import UserSerializer
from users.models import CustomUser


class CreateUserView(CreateAPIView):
    model = CustomUser
    serializer_class = UserSerializer

    permission_classes = [
        permissions.AllowAny
    ]
