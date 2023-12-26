from django import forms
from models import Choice


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ["text"]
