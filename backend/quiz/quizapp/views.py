from rest_framework import viewsets

from .serializers import UserAnswerSerializer, QuizSerializer
from .models import UserAnswer, Quiz


class UserAnswerViewSet(viewsets.ModelViewSet):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer