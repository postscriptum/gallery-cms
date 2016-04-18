from django.shortcuts import render
from .models import General


def main(request):
    if General.objects.count() > 0:
        general = General.objects.all()[0]
        if general.under_construction:
            # UNDER CONSTRUCTION page
            context = {'comment': 'Coming back soon'}
            return render(request, 'front/under_construction.html', context)
        # NORMAL page
        context = {
            'general': general
        }
        return render(request, 'front/main.html', context)
    else:
        # ERROR page
        context = {'error_description': 'No general site settings'}
        return render(request, 'front/error.html', context)
