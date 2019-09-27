from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import (
    UserSerializer,
    UserAnswerSerializer,
    TopUserSerializer
)
from .models import (
    User,
    UserAnswer
)
from quizapp.serializers import (
    QuizSerializerWithoutQuestions,
    UserQuizAnswerSerializer,
    QuestionWithOnlyIdAndAnswersSerializer
)
from quizapp.models import Quiz


h201 = status.HTTP_201_CREATED
h400 = status.HTTP_400_BAD_REQUEST
h204 = status.HTTP_204_NO_CONTENT


class UserViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer

    """
    List users
    """
    def list(self, request):
        queryset = User.objects.all()
        users = get_list_or_404(queryset)
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)

    """
    Create user
    """
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=h201)
        else:
            return Response(serializer.errors, status=h400)

    """
    Get user
    """
    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)


class QuizAnswerViewSet(viewsets.ViewSet):
    serializer_class = UserAnswerSerializer

    """
    Create quiz answer
    """
    def create(self, request):
        is_many = isinstance(request.data, list)
        if is_many:
            serializer = self.serializer_class(data=request.data, many=True)
        else:
            serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=h201)
        else:
            return Response(serializer.errors, status=h400)


class UserQuizAnswerViewSet(viewsets.ViewSet):
    serializer_class = UserQuizAnswerSerializer

    """
    User quizzes list when answered
    """
    def list(self, request, user_pk=None):
        queryset = UserAnswer.objects.all()
        user_answers = get_list_or_404(queryset, user=user_pk)
        data = []
        for user_answer in user_answers:
            data.append(user_answer.quiz.pk)

        quizzes = Quiz.objects.filter(pk__in=data)
        serializer = QuizSerializerWithoutQuestions(quizzes, many=True)
        return Response(serializer.data)

    """
    Get quiz user answers
    """
    def retrieve(self, request, pk=None, user_pk=None):
        queryset = UserAnswer.objects.all()
        quiz_answered_questions = get_list_or_404(queryset, user=user_pk, quiz=pk)

        data = []
        question_data = []
        for answered_question in quiz_answered_questions:
            question_data.append(answered_question.question.pk)

        for question in question_data:
            queryset = UserAnswer.objects.all()
            quiz_answered_question_answer = get_object_or_404(queryset, user=user_pk, quiz=pk, question=question)
            data.append({
                'id': question,
                'answer': quiz_answered_question_answer.answer
            })

        serializer = QuestionWithOnlyIdAndAnswersSerializer(data, many=True)
        return Response(serializer.data)


class TopUserViewSet(viewsets.ViewSet):
    serializer_class = TopUserSerializer

    """
    Top users
    """
    def list(self, request):
        users = User.objects.all()
        serializer = TopUserSerializer(users, many=True)
        return Response(serializer.data)