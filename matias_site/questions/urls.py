from django.urls import path
from questions import views

app_name = "questions"

urlpatterns = [
    path("questions/", views.QuestionView.as_view(), name="questions"),
    path("", views.index, name="colis"),
    path("code/", views.CodeView.as_view(), name="code"),
]