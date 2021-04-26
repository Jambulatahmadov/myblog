from django.shortcuts import render, redirect
from .models import MyNews
from django.views.generic import DetailView
from .forms import MyNewsForm


class NewsDetail(DetailView):
    model = MyNews
    template_name = 'news/detail_views.html'
    context_object_name = 'mynews'


def create(request):
    error = ''
    if request.method == 'POST':
        form = MyNewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Не верная форма!'

    form = MyNewsForm

    date = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', date)


def index(request):
    news = MyNews.objects.order_by('-date')
    return render(request, 'news/index.html', {'news': news})

