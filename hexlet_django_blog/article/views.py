from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from hexlet_django_blog.article.models import Article, Comment


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'show.html', context={
            'article': article,
        })

  
class ArticleCommentsView(View):

    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=kwargs['id'], article__id=kwargs['article_id'])
        return render(request, 'show.html', context={
            'comment': comment,
        })


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'article/index.html', context={
            'articles': articles,
        })

def index(request, tags, article_id):
    return render(
        request,
        'article/index.html',
        context={'tags':tags, 'article_id': article_id},
        )

def redirect_view(request):
    response = redirect(reverse('article', kwargs = {'tags':'Python', 'article_id':41}))
    return response