from http.client import HTTPResponse

from colis.forms import AnswerForm
from colis.models import Choice, Question
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from rest_framework.request import Request

# Create your views here.


def quiz(request: Request, question_number: int = 1) -> HTTPResponse:
    question = Question.objects.get(pk=question_number)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            user_answer = form.cleaned_data["text"]
            correct_option = Choice.objects.get(question=question, is_correct=True)
            if user_answer == correct_option.text:
                if question_number < 3:
                    return redirect("quiz", question_number=question_number + 1)
                else:
                    return redirect("result")
    else:
        form = AnswerForm()

    return render(request, "quiz_app/quiz.html", {"question": question, "form": form})


def result(request: Request):
    return render(request, "quiz_app/result.html")
