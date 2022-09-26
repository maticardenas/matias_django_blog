from django import forms
from blog.models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "author",
            "title",
            "text",
        )

        # widgets here allow us to link fields to bootstrap and then being rendered properly
        # when we use for instance {{ form.as_p }} at the django template.
        widgets = {
            "author": forms.Select(attrs={"class": "btn-group"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "editable medium-editor-textarea postcontent"}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            "author",
            "text",
        )

        widgets = {
            "author": forms.TextInput(attrs={"class": "textinputclass"}),
            "text": forms.Textarea(attrs={"class": "editable medium-editor-textarea"}),
        }
