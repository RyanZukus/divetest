from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)