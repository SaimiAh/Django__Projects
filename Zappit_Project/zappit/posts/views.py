from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)