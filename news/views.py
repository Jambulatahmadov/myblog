from django.shortcuts import render
from .models import MyNews
from django.http import HttpResponse


def index(request):
    news = MyNews.objects.all()
    return render(request, 'news/index.html', {'news': news})


def about(request):
    news = MyNews.objects.all()
    return render(request, 'news/about.html', {'news': news})
