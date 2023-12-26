from questions.models import Names, Question
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("name", "code", "answer")


class CodeSerializer(serializers.Serializer):
    name = serializers.ChoiceField(choices=Names.choices)
    answer = serializers.CharField(max_length=200)
