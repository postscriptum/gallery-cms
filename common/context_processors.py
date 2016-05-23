from front.models import General


def general(request):
    context = {}
    if General.objects.count() > 0:
        context['general'] = General.objects.all()[0]
    return context
