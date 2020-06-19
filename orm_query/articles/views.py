from django.views.generic import ListView
from django.shortcuts import render

from .models import Article


def articles_list(request):
    template_name = 'articles/news.html'
    context = {
        'object_list': Article.objects.order_by('-published_at')\
            .defer('published_at')\
            .select_related('genre', 'author').all()
    }
    return render(request, template_name, context)
