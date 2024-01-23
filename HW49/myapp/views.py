from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .models import Task
from django.contrib.auth.models import User
from .serializers import TaskSerializer, UserSerializer

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer