from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    source = models.CharField(max_length=200)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

