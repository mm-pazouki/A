from django.shortcuts import render
from .models import Todo


def home(request):
    all = Todo.objects.all()
    return render(request, 'root.html', {'todos': all})


def say_hello(request):
    person = {'name': 'mehdi'}
    return render(request, 'home.html', context=person)
