from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializers


class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializers

    def get_queryset(self):
        return Post.objects.all()


class BlogPostCreateView(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializers

    def get_queryset(self):
        return Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogPostListView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializers

    def get_queryset(self):
        return Post.objects.all()


class BlogPostRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializers

    def get_queryset(self):
        return Post.objects.all()

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class BlogPostRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializers

    def get_queryset(self):
        return Post.objects.all()

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
