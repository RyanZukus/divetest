from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path('', views.main, name='main'),
    path('write/', views.write, name='write'),
    path('article/<int:article_id>', views.article, name='article'),
]
