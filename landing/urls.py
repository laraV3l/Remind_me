from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('task',views.task, name='task-page'),
        ]
