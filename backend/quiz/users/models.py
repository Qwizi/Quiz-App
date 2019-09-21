from django.db import models
from quizapp.models import Quiz, Question, Answer


class User(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)