from rest_framework import serializers
from questions.models import Question

from questions.models import Names


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("name", "code", "answer")


class CodeSerializer(serializers.Serializer):
    name = serializers.ChoiceField(choices=Names.choices)
    answer = serializers.CharField(max_length=200)