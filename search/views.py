from django.shortcuts import render
from blog.models import Post


def search(request):
    q = request.GET.get('q')
    posts = Post.objects.filter(title__search=q)

    return render(request, 'search/search.html', {'posts': posts})
