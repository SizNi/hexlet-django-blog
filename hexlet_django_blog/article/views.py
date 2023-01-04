from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from hexlet_django_blog.article.models import Article, Comment
from .forms import CommentArticleForm
from django.forms import ModelForm

"""class ArticleCommentFormView(View):

    def post(self, request, *args, **kwargs):
        # Получаем данные формы из запроса
        form = ArticleCommentForm(request.POST)
        if form.is_valid(): # Проверяем данных формы на корректность
            form.save() # Сохраняем форм"""
class ArticleFormDestroyView(View):

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        articel = Article.objects.get(id=article_id)
        if articel:
            articel.delete()
        return redirect('articles')
    
     
class ArticleFormUpdateView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'update.html', {'form': form, 'article_id':article_id})
    
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles')

        return render(request, 'update.html', {'form': form, 'article_id':article_id})


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']



class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid(): # Если данные корректные, то сохраняем данные формы
            form.save()
            return redirect('articles') # Редирект на указанный маршрут
        # Если данные некоректные, то возвращем человека обратно на страницу с заполенной формой
        return render(request, 'create.html', {'form': form})


class CommentArticleView(View):

    def get(self, request, *args, **kwargs):
        form = CommentArticleForm() # Создаем экземпляр нашей формы
        return render(request, 'comment.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = CommentArticleForm(request.POST) # Получаем данные формы из запроса
        if form.is_valid(): # Проверяем данных формы на корректность
            comment = Comment(
                name = form.cleaned_data['comment'], # Получаем очищенные данные из поля name
                        # Заполняем оставшиеся поля
                )
            comment.save()


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