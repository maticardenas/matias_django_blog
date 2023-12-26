from rest_framework.request import Request

from blog.forms import CommentForm, PostForm
from blog.models import Comment, Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from pathlib import Path
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

CURRENT_DIR = Path(__file__).resolve().parent
MD_POSTS = CURRENT_DIR / "md_posts"


# class HighlightRenderer(mistune.HTMLRenderer):
#     def block_code(self, code, info=None):
#         if info:
#             lexer = get_lexer_by_name(info, stripall=True)
#             formatter = html.HtmlFormatter()
#             # return highlight(code, lexer, formatter)
#             return '<pre><code>' + highlight(code, lexer, formatter) + '</code></pre>'
#         return '<pre><code>' + mistune.escape(code) + '</code></pre>'
#     def text(self, text):
#         return '<pre><code>' + mistune.escape(text) + '</code></pre>'
#
# renderer = HighlightRenderer()
# markdown = mistune.create_markdown(renderer=renderer)


class PostDetailView(DetailView):
    model = Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")


# def post_detail(request: Request, file_name: str) -> "Response":
#     file = MD_POSTS / f"{file_name}.md"
#     print(f"MARKDOWN CONTENT:\n\n {file.read_text()}\n\n")
#
#     html_content = markdown(file.read_text()).replace('\n', '<br>') #mistune.html(file.read_text())
#
#     print(f"HTML CONTENT:\n\n {html_content}\n\n")
#
#     return render(request, "blog/post_detail.html", {"post": html_content})


# def post_detail(request: Request, pk: int) -> "Response":
#     post = get_object_or_404(Post, pk=pk)
#
#     post_html_content_text = mistune.html(post.text)#markdown(post.text).
#
#     return render(request, "blog/post_detail.html", {"post": post_html_content_text})


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
        return Post.objects.filter(published_date__isnull=True).order_by("create_date")


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
