from front.models import General
from catalog.models import Article


def general(request):
    context = {
        'articles': Article.objects.filter(enabled=True)
    }
    if General.objects.count() > 0:
        context['general'] = General.objects.all()[0]
    return context
