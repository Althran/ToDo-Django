from django.urls import path
from .views import MainView, DeleteTaskView, UpdateTaskView, TaskView, EditTaskView


urlpatterns = [
    path('', MainView.as_view(), name='tasks'),
    path('delete/<pk>/', DeleteTaskView.as_view(), name='delete'),
    path('update/<pk>/', UpdateTaskView.as_view(), name='update'),
    path('view/<pk>/', TaskView.as_view(), name='view'),
    path('edit/<pk>/', EditTaskView.as_view(), name='edit'),
]
