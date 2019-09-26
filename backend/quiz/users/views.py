from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import UserSerializer, UserAnswerSerializer
from .models import User, UserAnswer
from quizapp.serializers import QuizSerializerWithoutQuestions, UserQuizAnswerSerializer, QuestionWithOnlyIdAndAnswersSerializer
from quizapp.models import Answer, Question, Quiz
# from quizapp.models import Quiz, Question, Answer
# from quizapp.serializers import (
#    UserQuizSerializer,
#    UserQuestionSerializer,
#    UserAnswerSerialier as QuizUserAnswerSerializer
# )


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
    # data = []
    # quiz_data = []
    # question_data = []
    # answer_data = []

    # for user_answer in user_answers:
    #    quiz_data.append(user_answer.quiz.pk)
    #    question_data.append(user_answer.question.pk)
    #    answer_data.append(user_answer.answer.pk)

    # for quiz in quiz_data:
    #    data.append({
    #        'title': Quiz.objects.values('title').get(pk=quiz),
    #        'questions': Question.objects.filter(pk__in=question_data),
    #        'answers': Answer.objects.filter(pk__in=answer_data)
    #    })
    #serializer = self.serializer_class(data, many=True)
    #return Response(serializer.data)

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
        answer_data = []
        for answered_question in quiz_answered_questions:
            question_data.append(answered_question.question.pk)
            # answer_data.append(answered_question.answer.pk)

        for question in question_data:
            queryset = UserAnswer.objects.all()
            quiz_answered_question_answer = get_object_or_404(queryset, user=user_pk, quiz=pk, question=question)
            data.append({
                'id': question,
                'answer': quiz_answered_question_answer.answer
            })

        serializer = QuestionWithOnlyIdAndAnswersSerializer(data, many=True)
        return Response(serializer.data)
"""
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
"""