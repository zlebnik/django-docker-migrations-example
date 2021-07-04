from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):
    name = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(default='')
    completed = models.BooleanField(default=False)
