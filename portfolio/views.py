from django.shortcuts import render, redirect
from .models import Project, Introduction
from urllib.parse import urljoin
from django.http import Http404


def index(request):
    context = {
        'projects': Project.objects.all().order_by('-id'),
        'empty_block': False,
    }
    try:
        introduction_object = Introduction.objects.get()
        context['intro_object'] = introduction_object
    except Introduction.DoesNotExist:
        pass
    if context['projects'].count() % 3 == 2:
        context['empty_block'] = True
    return render(request, 'portfolio/index.html', context=context)


def introduction_admin(request):
    try:
        introduction_object = Introduction.objects.get()
    except Introduction.DoesNotExist:
        return redirect(urljoin(request.get_full_path(), "add"))
    return redirect(urljoin(request.get_full_path(), f"{introduction_object.id}/change"))


def handler404(request, exception=None):
    return redirect('index')
