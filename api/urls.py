from django.urls import path
from .views import TodoList, TodoDetail

urlpatterns = [
    path('api/todos/', TodoList.as_view(), name='todo-list'),
    path('api/todos/<int:pk>/', TodoDetail.as_view(), name='todo-detail'),
]

