from django.db import models
from django.conf import settings


# Create your models here.

class Question(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.answer
