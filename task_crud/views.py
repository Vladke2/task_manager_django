from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .serializers import TaskCreateSerializer, TaskListRetrieveUpdateDestroySerializer
from .models import Task
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter


class TaskCreateAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskCreateSerializer
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskRetrieveAPIView(RetrieveAPIView):
    serializer_class = TaskListRetrieveUpdateDestroySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskListAPIView(ListAPIView):
    serializer_class = TaskListRetrieveUpdateDestroySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskSearchAPIView(ListAPIView):
    serializer_class = TaskListRetrieveUpdateDestroySerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ['title']

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskListRetrieveUpdateDestroySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
