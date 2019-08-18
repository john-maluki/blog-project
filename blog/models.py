from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex
from django.db import models
from django.urls import reverse
from search.search import BlogPostIndex

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    body = models.TextField()
    # search = SearchVectorField(null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[str(self.pk)])

    def get_api_url(self):
        return reverse('post_rud', kwargs={'pk': self.pk})

    # Add indexing method to BlogPost
    def indexing(self):
        obj = BlogPostIndex(
            index={'id': self.id},
            title=self.title,
            author=self.author.username,
            body=self.body
        )
        obj.save()
        return obj.to_dict(include_meta=True)
