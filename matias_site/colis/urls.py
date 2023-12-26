from colis.views import quiz
from django.urls import path

urlpatterns = [
    path("quiz/<int:quiz_id>/<int:question_id>/", quiz, name="quiz"),
]
