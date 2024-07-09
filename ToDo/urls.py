from django.urls import path

from ToDo.apps import TodoConfig
from ToDo.views import TaskCreateAPIView, TagCreateAPIView, TaskListAPIView, TaskRetrieveAPIView, TaskUpdateAPIView, \
    TaskDestroyAPIView, TagListAPIView, TagUpdateAPIView, TagDestroyAPIView, TaskRetrieveViewByUUID

app_name = TodoConfig.name

urlpatterns = [
    path('task/create/', TaskCreateAPIView.as_view(), name='task-create'),
    path('tasks/', TaskListAPIView.as_view(), name='tasks-list'),
    path('task/<int:pk>/', TaskRetrieveAPIView.as_view(), name='task-detail'),

    path('task/<uuid:uuid>/', TaskRetrieveViewByUUID.as_view(), name='task-uuid'),

    path('task/update/<int:pk>/', TaskUpdateAPIView.as_view(), name='tasks-update'),
    path('task/delete/<int:pk>/', TaskDestroyAPIView.as_view(), name='tasks-delete'),

    path('tag/create/', TagCreateAPIView.as_view(), name='tag-create'),
    path('tags/', TagListAPIView.as_view(), name='tags'),
    path('tag/update/<int:pk>/', TagUpdateAPIView.as_view(), name='tag-update'),
    path('tag/delete/<int:pk>/', TagDestroyAPIView.as_view(), name='tag-delete'),

]
