import json

from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from rest_framework import generics

from questions.serializers import QuestionSerializer, CodeSerializer
from pathlib import Path

from rest_framework.response import Response

CURRENT_DIR = Path(__file__).resolve().parent
IMAGES_DIR = CURRENT_DIR / "images"

# Create your views here.

CODES = {
    "Kun": "5656", #
    "David": "3232", #
    "Pollo": "4444",
    "Pipi": "6262",
    "Ulises": "7171",
    "Pela": "7878",
}

CODE_ANSWERS = {
    "David": 52,
    "Ulises": 49,
    "Kun": 51,
    "Pipi": 42,
    "Pollo": 24,
    "Pela": 25,
}


CODE_IMAGES = {
    "Kun": "kun_question.png", #
    "David": "david_question.png", #
    "Pollo": "pollo_question.png",
    "Pipi": "pipi_question.png",
    "Ulises": "ulises_question.png",
    "Pela": "pela_question.png",
}

ANSWERS = {
    "Kun": 2, # Palermo + Enzo
    "David": 12, # Messi + Penaldo - Klose
    "Pollo": 31, # Ronald + Klose - Garce
    "Pipi": "marcos",
    "Ulises": "marcos",
    "Pela": "marcos",
}

IMAGES = {
    "Kun": "kun_answer.png", #
    "David": "david_answer.png", #
    "Pollo": "pollo_answer.png",
    "Pipi": "pipi_answer.png",
    "Ulises": "ulises_answer.png",
    "Pela": "pela_answer.png",
}



def index(request):
    return render(request, "colis_home.html")


class CodeView(generics.CreateAPIView):
    serializer_class = CodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        if int(data["answer"]) == int(CODE_ANSWERS[data["name"]]):
            image = CODE_IMAGES[data["name"]]
            file_handle = open(IMAGES_DIR / image, 'rb')
            response = FileResponse(file_handle, content_type='image/jpeg')

            return response
        else:
            return HttpResponse(f"Respuesta incorrecta para {data['name']}. Fijate bien cuando hablamos!", status=400, content_type="")


class QuestionView(generics.CreateAPIView):
    serializer_class = QuestionSerializer


    def check_answer(self, data):
        if data["name"] in ["Pipi", "Ulises"]:
            return data["answer"].lower() == ANSWERS[data["name"]]
        elif data["name"] in ["Pela"]:
            return data["answer"].lower() in ["krkic", "krkić"]
        else:
            return int(data["answer"]) == int(ANSWERS[data["name"]])
    def create(self, requests, *args, **kwargs):
        serializer = self.get_serializer(data=requests.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        if int(data["code"]) != int(CODES[data["name"]]):
            return HttpResponse(f"Codigo incorrecto para {data['name']}", status=400, content_type="")

        if not self.check_answer(data):
            return HttpResponse(f"Respuesta incorrecta para {data['name']}", status=400, content_type="")

        image = IMAGES[data["name"]]

        file_handle = open(IMAGES_DIR / image, 'rb')
        response = FileResponse(file_handle, content_type='image/jpeg')
        # response['Content-Disposition'] = f'attachment; filename="{image}"'

        return response

