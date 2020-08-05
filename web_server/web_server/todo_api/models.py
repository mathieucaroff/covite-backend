from django.contrib.auth.models import User
from django.db import models

class Ressource(models.Model):
    class Meta:
        abstract = True
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class TodoGroup(Ressource):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

class TodoItem(Ressource):
    name = models.CharField(max_length=200)
    ticked_off = models.BooleanField()
    group = models.ForeignKey(to=TodoGroup, on_delete=models.CASCADE)
