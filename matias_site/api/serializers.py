from blog.models import Post
from rest_framework import serializers


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = [
            "text",
        ]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["author", "title", "text", "create_date", "published_date"]

    def get_fields(self):
        fields = super().get_fields()
        exclude_fields = self.context.get("exclude_fields", [])
        for field in exclude_fields:
            fields.pop(field, default=None)

        return fields
