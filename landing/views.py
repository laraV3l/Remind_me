from django.shortcuts import render
from django.http import HttpResponse
from .models import Remind

# Create your views here.

def home(request):
    return render(request,'landing/index.html')

def login(request):
    pass

def task(request):
    return render(request, "landing/task.html",context={ 'take': Remind.objects.all()})