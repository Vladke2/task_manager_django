import django.contrib.auth.models
from django.db import models
from base_model import CommonBaseModel


class Task(CommonBaseModel):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    user = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title
