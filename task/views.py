from django.shortcuts import render
from rest_framework import generics, serializers, permissions
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework import exceptions
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsManagerOrReadOnly, IsAdminOrReadOnly
from .permissions import IsManagerOrAuthenticated, IsAdminOrAuthenticated
from .permissions import IsSuperUser, IsManager


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_permissions(self):
        match self.action:
            case 'create':
                permission_classes = [IsSuperUser]
            case 'update' | 'partial_update' | 'delete':
                permission_classes = [IsManager]
            case _:
                permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
        

'''
# change from ListAPIView to ListCreateAPIView, will enable new record creation
#class ListTasks(generics.ListAPIView):
class ListTasks(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAdminOrAuthenticated,)

# change from RetrieveAPIView to RetrieveUpdateDestroyAPIView, enable update and delete
#class DetailTask(generics.RetrieveAPIView):
class DetailTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsManagerOrAuthenticated,)
'''