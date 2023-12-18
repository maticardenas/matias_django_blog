from django.db import models

class Quiz(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_img = models.ImageField(upload_to='images/', blank=True)
    order = models.IntegerField()
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)

    answer = models.CharField(max_length=200)

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text