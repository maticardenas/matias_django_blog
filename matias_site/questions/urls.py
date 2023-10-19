from django.urls import path
from questions import views

app_name = "questions"

urlpatterns = [
    path("", views.QuestionView.as_view(), name="questions"),
    path("code/", views.CodeView.as_view(), name="code"),
]