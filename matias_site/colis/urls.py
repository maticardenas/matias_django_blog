from django.urls import path

from colis.views import quiz


urlpatterns = [
    path("quiz/<int:quiz_id>/<int:question_id>/", quiz, name='quiz'),
]