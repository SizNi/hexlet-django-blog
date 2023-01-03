from django.urls import path
from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import IndexView, ArticleView, ArticleCommentsView

urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:id>/', ArticleView.as_view()),
    path('<int:article_id>/comments/<int:id>/', ArticleCommentsView.as_view()),
]