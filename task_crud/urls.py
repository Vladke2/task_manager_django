from django.urls import path
from .views import TaskCreateAPIView, TaskListAPIView, TaskRetrieveUpdateDestroyAPIView, TaskRetrieveAPIView, \
    TaskSearchAPIView


urlpatterns = [
    path('create/', TaskCreateAPIView.as_view()),
    path('my/', TaskListAPIView.as_view()),
    path('manage_task/', TaskRetrieveUpdateDestroyAPIView.as_view()),
    path('<int:pk>/', TaskRetrieveAPIView.as_view()),
    path('search/', TaskSearchAPIView.as_view()),

]
