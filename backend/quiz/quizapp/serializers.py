from rest_framework import serializers
from .models import Quiz, Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'content', 'answers', 'correct_answer']


class QuestionSerializerWithoutAnswers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'content']


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'questions']


class QuizSerializerWithoutQuestions(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'title']