from api.serializers import PostSerializer
from blog.models import Post
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
