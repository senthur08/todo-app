from django.urls import path
from . import views

urlpatterns = [
    path('', views.lists, name='todo-index'),
    path('update_task/<str:pk>', views.updateTask, name='todo-update'),
    path('delete/<str:pk>', views.delete, name='todo-delete'),
]