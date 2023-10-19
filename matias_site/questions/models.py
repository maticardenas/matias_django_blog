from django.db import models

# Create your models here.


class Names(models.TextChoices):
    EMA = "Ema"
    DAVID = "David"
    FEDE = "Fede"


class Question(models.Model):
    name = models.CharField(choices=Names.choices, max_length=200)
    code = models.CharField(max_length=4)
    answer = models.CharField(max_length=200)
