from rest_framework import serializers
from django.utils.timezone import now
from .models import Task


class TaskCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Task
        fields = '__all__'

    def validate_deadline(self, value):
        if value <= now():
            raise serializers.ValidationError("Дата має бути пізніше за сьогодні")
        return value


class TaskListRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Task
        fields = '__all__'
