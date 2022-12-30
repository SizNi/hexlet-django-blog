from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path('article/', views.index),
    path('', views.index),
]