from django.db import models
from user.models import User


class Answer(models.Model):
    content = models.CharField(max_length=80)

    def __str__(self):
        return self.content


class Question(models.Model):
    content = models.CharField(max_length=80)
    answers = models.ManyToManyField(Answer, related_name='question_answers')
    correct_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Quiz(models.Model):
    title = models.CharField(max_length=80)
    questions = models.ManyToManyField(Question, related_name='quiz_questions')

    def __str__(self):
        return self.title


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)