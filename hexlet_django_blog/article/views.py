from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    tags = 'Hexlet-django-blog'
    return render(
        request,
        'article/index.html',
        context={'tags':tags},
        )
