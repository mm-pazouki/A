from django.shortcuts import render

def home(request):
    return  render(request, 'root.html')

def say_hello(request):
    person = {'name': 'mehdi'}
    return render(request, 'home.html', context=person)