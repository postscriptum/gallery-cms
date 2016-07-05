from django.shortcuts import render, get_object_or_404
from catalog.models import Gallery, Article


def main(request):
    context = {
        'galleries': Gallery.objects.filter(enabled=True).order_by('order')
    }
    return render(request, 'front/main.html', context)


def get_article(request, slug):
    context = {
        'article': get_object_or_404(Article, slug=slug, enabled=True)
    }
    return render(request, 'front/article.html', context)
