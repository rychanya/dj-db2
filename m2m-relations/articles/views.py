from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.order_by('-published_at').all().prefetch_related('tagsarticles_set')
    context = {
        'object_list': articles
    }
    return render(request, template, context)
