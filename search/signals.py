from django.contrib.postgres.search import SearchVector
from django.db.models.signals import post_save
from django.dispatch import receiver

from blog.models import Post


@receiver(post_save, sender=Post)
def update_search_vector(sender, instance, **kwargs):
    Post.objects.filter(pk=instance.pk).update(search=SearchVector('title'))
