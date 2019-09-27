from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import QuizSerializer
from .models import Quiz


class QuizViewSet(viewsets.ViewSet):
    serializer_class = QuizSerializer

    """
    List quizzes
    """
    def list(self, request):
        quizzes = Quiz.objects.all()
        serializer = self.serializer_class(quizzes, many=True)
        return Response(serializer.data)

    """
    Get quiz info
    """
    def retrieve(self, request, pk=None):
        queryset = Quiz.objects.all()
        quiz = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(quiz)
        return Response(serializer.data)