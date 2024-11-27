from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import News, Category
from .forms import NewsForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy


class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')



# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news, 
#         'title': 'Главная страница - Список новостей'
#     }
#     return render(request, 'news/index.html', context)

class NewsByCategory(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['category_slug'])

        return context
    
    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        category = get_object_or_404(Category, slug=category_slug)
        return News.objects.filter(category=category, is_published=True).select_related('category')

    
    
# def get_category(request, category_slug): 
#     category = Category.objects.get(slug=category_slug)
#     news = News.objects.filter(category=category)
#     context = {
#         'news': news, 
#         'category': category
#     }
#     return render(request, 'news/category.html', context)

# def view_news(request, news_slug):
#     news = News.objects.get(slug=news_slug)
    
#     context = {
#         'news_item': news
#     }
#     return render(request, 'news/view_news.html', context)

# class ViewNews(DetailView):
#     model = News
#     slug_url_kwarg = 'news_slug'
#     template_name = 'news/view_news.html'
#     context_object_name = 'news_item'

class ViewNews(DetailView):
    model = News
    # pk_url_kwarg = 'news_id'
    context_object_name = 'news_item'
    

# def view_news(request, news_slug):
#     try:
#         news = News.objects.get(slug=news_slug)
#     except News.DoesNotExist:
#         if 'add-news' in request.path:
#             return add_news(request)
#         else:
#             return render(request, '404.html', status=404)
    
#     context = {
#         'news_item': news
#     }
#     return render(request, 'news/view_news.html', context)

class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'

# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # news_item = News.objects.create(**form.cleaned_data)
#             news_item = form.save()
#             return redirect(news_item)
#     else: 
#         form = NewsForm() 
#     context = {
#         'form': form
#     }

#     return render(request, 'news/add_news.html', context)

