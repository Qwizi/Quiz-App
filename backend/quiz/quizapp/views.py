from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from django.shortcuts import get_object_or_404

from .serializers import (
    QuizSerializerWithoutQuestions,
    QuestionSerializerWithoutAnswers,
    AnswerSerializer,
    QuizSerializer
)

from users.serializers import UserAnswerSerializer

from .models import Quiz, Question

h201 = status.HTTP_201_CREATED
h400 = status.HTTP_400_BAD_REQUEST
h204 = status.HTTP_204_NO_CONTENT


class QuizViewSet(viewsets.ViewSet):
    serializer_class = QuizSerializer

    """
    List quizzes
    /quiz/
    """
    def list(self, request):
        quizzes = Quiz.objects.all()
        serializer = self.serializer_class(quizzes, many=True)
        return Response(serializer.data)

    """
    Get quiz info
    /quiz/{quiz_pk}/
    """
    def retrieve(self, request, pk=None):
        queryset = Quiz.objects.all()
        quiz = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(quiz)
        return Response(serializer.data)

"""
class QuizViewSet(viewsets.ViewSet):
    serializer_class = QuizSerializerWithoutQuestions

    def list(self, request):
        quizzes = Quiz.objects.all()
        serializer = self.serializer_class(quizzes, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Quiz.objects.all()
        quiz = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(quiz)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def all(self, request, pk=None):
        quiz = Quiz.objects.get(pk=pk)
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def answer(self, request):
        is_many = isinstance(request.data, list)
        if is_many:
            serializer = UserAnswerSerializer(data=request.data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=h204)
            else:
                return Response(serializer.errors, status=h400)
        else:
            serializer = UserAnswerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=h204)
            else:
                return Response(serializer.errors, status=h400)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=h201)
        else:
            return Response(serializer.errors, status=h400)
    def destroy(self, request, pk=None):
        quiz = Quiz.objects.get(pk=pk)
        quiz.delete()
        return Response(status=h204)
        
class QuestionViewSet(viewsets.ViewSet):
    serializer_class = QuestionSerializerWithoutAnswers

    def list(self, request, quiz_pk=None):
        quiz = Quiz.objects.get(pk=quiz_pk)
        questions = quiz.questions.all()
        serializer = self.serializer_class(questions, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, quiz_pk=None):
        quiz = Quiz.objects.get(pk=quiz_pk)
        queryset = quiz.questions.all()
        question = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(question)
        return Response(serializer.data)


class AnswerViewSet(viewsets.ViewSet):
    serializer_class = AnswerSerializer

    def list(self, request, quiz_pk=None, question_pk=None):
        quiz = Quiz.objects.get(pk=quiz_pk)
        queryset = quiz.questions.all()
        question = get_object_or_404(queryset, pk=question_pk)
        answers = question.answers.all()
        serializer = self.serializer_class(answers, many=True)
        return Response(serializer.data)
"""