from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from django.urls import reverse



def index(request, tags, article_id):
    return render(
        request,
        'article/index.html',
        context={'tags':tags, 'article_id': article_id},
        )

def redirect_view(request):
    response = redirect(reverse('article', kwargs = {'tags':'Python', 'article_id':41}))
    return response