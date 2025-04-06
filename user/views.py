from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .serializer import UserCreateSerializer, UserRetrieveUpdateDestroySerializer


class UserCreateAPIView(CreateAPIView):
    permission_classes = (AllowAny, )
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):
        serializer.save()


class UserRetrieveAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserRetrieveUpdateDestroySerializer

    def get_object(self):
        return self.request.user


class UserUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserRetrieveUpdateDestroySerializer

    def get_object(self):
        return self.request.user
