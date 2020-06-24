from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy
# Create your views here.

class TodoList(ListView):
    template_name = 'Todo/list.html'
    model = TodoModel

class Post_Detail(DetailView):
    template_name = 'Todo/detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'Todo/create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('todolist')

class TodoDelete(DeleteView):
    template_name = 'Todo/delete.html'
    model = TodoModel
    success_url = reverse_lazy('todolist')

class TodoUpdate(UpdateView):
    template_name = 'Todo/update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('todolist')