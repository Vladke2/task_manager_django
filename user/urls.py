from django.urls import path
from .views import UserCreateAPIView, UserUpdateDestroyAPIView, UserRetrieveAPIView


urlpatterns = [
    path('create/', UserCreateAPIView.as_view()),
    path('profile/', UserRetrieveAPIView.as_view()),
    path('edit/', UserUpdateDestroyAPIView.as_view()),
]
