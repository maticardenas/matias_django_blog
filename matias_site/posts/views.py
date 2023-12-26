from blog.models import Post
from django.shortcuts import render
from posts.serializers import PostListSerializer, PostSerializer

# Create your views here.
from rest_framework import views, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if self.action == "list":
            context["exclude_fields"] = ["text"]
        return context
