from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import TodoGroupSerializer, TodoItemSerializer, UserSerializer, GroupSerializer
from .models import TodoGroup, TodoItem

# from django.shortcuts import render

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class TodoGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows todo groups to be viewed or edited.
    """
    queryset = TodoGroup.objects.all()
    serializer_class = TodoGroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class TodoItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows todo items to be viewed or edited.
    """
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = [permissions.IsAuthenticated]


