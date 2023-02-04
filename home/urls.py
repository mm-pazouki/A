from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='root'),
    path('detail/<int:todo_id>/', views.detail, name='detail'),
    path('delete/<int:todo_id>', views.delete, name='delete'),
    path('create/', views.create, name='create'),
]

