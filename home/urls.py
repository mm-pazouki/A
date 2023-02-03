from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.say_hello),
]