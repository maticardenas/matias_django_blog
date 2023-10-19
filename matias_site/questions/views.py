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
    "Ema": "0912",
    "David": "1303",
    "Fede": "0777",
}

CODE_ANSWERS = {
    "Ema": 13,
    "David": 15,
    "Fede": 24,
}


CODE_IMAGES = {
    "Ema": "ema_code.jpg",
    "Fede": "fede_code.jpg",
    "David": "david_code.jpg",
}

ANSWERS = {
    "Ema": 14,
    "David": 818,
    "Fede": 2014,
}

IMAGES = {
    "Ema": "ema.jpg",
    "Fede": "fede.jpg",
    "David": "david.jpg",
}


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

    def create(self, requests, *args, **kwargs):
        serializer = self.get_serializer(data=requests.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        if int(data["code"]) != int(CODES[data["name"]]):
            return HttpResponse(f"Codigo incorrecto para {data['name']}", status=400, content_type="")

        if int(data["answer"]) != int(ANSWERS[data["name"]]):
            return HttpResponse(f"Respuesta incorrecta para {data['name']}", status=400, content_type="")

        image = IMAGES[data["name"]]

        file_handle = open(IMAGES_DIR / image, 'rb')
        response = FileResponse(file_handle, content_type='image/jpeg')
        # response['Content-Disposition'] = f'attachment; filename="{image}"'

        return response

