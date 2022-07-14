from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.db.models import Sum
from django.urls import reverse

from articles.models import Article

def main(request):
    articles = Article.objects.order_by('timestamp')
    return render(request, 'articles/main.html', {'articles': articles})

def write(request):
    if request.method == "POST":
        post = request.POST
        wr = Article(title=post.get('title'), author=post.get('author'), body_text=post.get('body_text'), timestamp=timezone.now())
        wr.save()
        articles = Article.objects.order_by('timestamp')
        return HttpResponseRedirect(reverse('articles:main'))
    return render(request, 'articles/write.html')

def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/article.html', {'article': article})