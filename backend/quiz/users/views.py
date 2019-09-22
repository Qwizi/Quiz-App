from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serializers import UserSerializer, UserAnswerSerializer
from .models import User, UserAnswer
from quizapp.models import Quiz, Question, Answer
from quizapp.serializers import (
    UserQuizSerializer,
    UserQuestionSerializer,
    UserAnswerSerialier as QuizUserAnswerSerializer
)


h201 = status.HTTP_201_CREATED
h400 = status.HTTP_400_BAD_REQUEST
h204 = status.HTTP_204_NO_CONTENT


class UserViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer

    def list(self, request):
        queryset = User.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=h201)
        else:
            return Response(serializer.errors, status=h400)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=h204)

class UserQuizViewSet(viewsets.ViewSet):
    serializer_class = UserQuizSerializer

    def list(self, request, user_pk=None):
        user = User.objects.get(pk=user_pk)
        user_answers = UserAnswer.objects.filter(user=user)
        data = []

        for answer in user_answers:
            data.append(answer.quiz.pk)

        quizzes = Quiz.objects.filter(pk__in=data)
        serializer = self.serializer_class(quizzes, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, user_pk=None):
        user = User.objects.get(pk=user_pk)
        quiz = Quiz.objects.get(pk=pk)
        serializer = self.serializer_class(quiz)
        return Response(serializer.data)


class UserQuestionViewSet(viewsets.ViewSet):
    serializer_class = UserQuestionSerializer

    def list(self, request, user_pk=None, quiz_pk=None):
        user = User.objects.get(pk=user_pk)
        quiz = Quiz.objects.get(pk=quiz_pk)
        user_answers = UserAnswer.objects.filter(user=user, quiz=quiz)
        data = []

        for answer in user_answers:
            data.append(answer.question.pk)

        questions = Question.objects.filter(pk__in=data)
        serializer = self.serializer_class(questions, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, user_pk=None, quiz_pk=None):
        user = User.objects.get(pk=user_pk)
        quiz = Quiz.objects.get(pk=quiz_pk)
        question = Question.objects.get(pk=pk)
        serializer = self.serializer_class(question)
        return Response(serializer.data)

class UserAnswerViewSet(viewsets.ViewSet):
    serializer_class = QuizUserAnswerSerializer

    def list(self, request, user_pk=None, quiz_pk=None, question_pk=None):
        user = User.objects.get(pk=user_pk)
        quiz = Quiz.objects.get(pk=quiz_pk)
        question = Question.objects.get(pk=question_pk)
        user_answers = UserAnswer.objects.filter(
            user=user,
            quiz=quiz,
            question=question
        )
        data = []

        for answer in user_answers:
            data.append(answer.answer.pk)

        answer = Answer.objects.get(pk__in=data)
        serializer = self.serializer_class(answer)
        return Response(serializer.data)
