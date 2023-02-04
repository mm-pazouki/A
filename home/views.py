from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm


def home(request):
    all = Todo.objects.all()
    return render(request, 'root.html', {'todos': all})


def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {'todo': todo})


def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, 'todo deleted successfully', 'success')
    return redirect('root')


def create(request):
    form = TodoCreateForm()
    return render(request, 'create.html', {'form':form})




