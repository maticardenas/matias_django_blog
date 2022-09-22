from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from forms import PostForm
from models import Post


class AboutView(TemplateView):
    template_name = "about.html"


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")


class PostDetailView(DetailView):
    models = Post


class CreatePostView(CreateView, LoginRequiredMixin):
    login_url = "/login/"
    redirect_field_name = "blog/post_detail.html"
    form_class = PostForm
    model = Post


class PostUpdateView(UpdateView, LoginRequiredMixin):
    login_url = "/login/"
    redirect_field_name = "blog/post_detail.html"
    form_class = PostForm
    model = Post


class PostDeleteView(DeleteView, LoginRequiredMixin):
    login_url = "/login/"
    success_url = reverse_lazy("post_list")
    model = Post


class DraftListView(ListView, LoginRequiredMixin):
    login_url = "/login/"
    redirect_field_name = "blog/post_list.html"
    model = Post

    def get_queryset(self):
        return Post.filter(publish_date__isnull=True).order_by("created_date")
