from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import (TodoGroup, TodoItem)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TodoGroupSerializer(serializers.HyperlinkedModelSerializer):
    items = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = TodoGroup
        fields = ['url', 'user', 'items']

class TodoItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoItem
        fields = ['url', 'name', 'ticked_off', 'group']
