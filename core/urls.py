from django.urls import path
from .views import MainView, DeleteTaskView, UpdateTaskView


urlpatterns = [
    path('', MainView.as_view(), name='tasks'),
    path('delete/<pk>/', DeleteTaskView.as_view(), name='delete'),
    path('update/<pk>/', UpdateTaskView.as_view(), name='update'),
]
