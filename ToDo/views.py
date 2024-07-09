from django.shortcuts import get_object_or_404
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from ToDo.models import Task, Tag
from ToDo.permissions import IsOwner
from ToDo.serializers import TaskSerializer, TagSerializer, TaskCreateSerializer


class TaskCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskCreateSerializer

    def perform_create(self, serializer):
        new_task = serializer.save()
        new_task.owner = self.request.user
        new_task.save()


class TaskListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'tag__title']

    # http://127.0.0.1:8000/tasks/?search


class TaskRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class TaskRetrieveViewByUUID(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, uuid=self.kwargs['uuid'])

        return obj


class TaskUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class TaskDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Task.objects.all()


class TagCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = TagSerializer


class TagListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    queryset = Tag.objects.all()


class TagUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = TaskSerializer
    queryset = Tag.objects.all()


class TagDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Tag.objects.all()
