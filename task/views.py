from django.shortcuts import render
from rest_framework import generics, serializers, permissions
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework import exceptions

from .models import Task
from .serializers import TaskSerializer
from .permissions import IsManagerOrReadOnly, IsAdminOrReadOnly

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_permissions(self):
        match self.action:
            case 'list' | 'create':
                permission_classes = [IsAdminOrReadOnly]
            case 'retrieve' | 'update' | 'partial_update' | 'delete':
                permission_classes = [IsManagerOrReadOnly]
            case _:
                raise exceptions.PermissionDenied
        return [permission() for permission in permission_classes]


'''
# change from ListAPIView to ListCreateAPIView, will enable new record creation
#class ListTasks(generics.ListAPIView):
class ListTasks(generics.ListCreateAPIView):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# change from RetrieveAPIView to RetrieveUpdateDestroyAPIView, enable update and delete
#class DetailTask(generics.RetrieveAPIView):
class DetailTask(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsManagerOrReadOnly,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    '''
