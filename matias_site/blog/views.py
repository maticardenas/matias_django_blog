from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)
from forms import CommentForm, PostForm
from models import Comment, Post


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


################################################################################


@login_required
def add_comment_to_post(request: "Request", pk: int) -> "Response":
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect("post_detail", pk=post.pk)
    else:
        form = CommentForm()

    return render(request, "blog/comment_form.html", {"form": form})


@login_required
def approve_comment(request: "Request", pk: int) -> "Response":
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()

    return redirect("post_detail", pk=comment.post.pk)


@login_required
def remove_comment(request: "Request", pk: int) -> "Response":
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()

    return redirect("post_detail", pk=post_pk)


@login_required
def publish_post(request: "Request", pk: int) -> "Response":
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect("post_detail", pk=post.pk)
