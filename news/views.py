from django.shortcuts import render
from .models import MyNews
from django.views.generic import DetailView


class NewsDetail(DetailView):
    model = MyNews
    template_name = 'news/detail_views.html'
    context_object_name = 'mynews'


def create(request):
    return render(request, 'news/create.html')


def index(request):
    news = MyNews.objects.order_by('-date')
    return render(request, 'news/index.html', {'news': news})


def about(request):
    news = MyNews.objects.order_by('-date')
    return render(request, 'news/about.html', {'news': news})
