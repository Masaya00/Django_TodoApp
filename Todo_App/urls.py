from django.contrib import admin
from django.urls import path
from .views import TodoList, Post_Detail, TodoCreate, TodoDelete, TodoUpdate


urlpatterns = [
    path('', TodoList.as_view(), name="todolist"),
    path('detail/<int:pk>', Post_Detail.as_view(), name="detail"),
    path('create/', TodoCreate.as_view(), name="create"),
    path('delete/<int:pk>', TodoDelete.as_view(), name='delete'),
    path('update/<int:pk>', TodoUpdate.as_view(), name='update'),
]
