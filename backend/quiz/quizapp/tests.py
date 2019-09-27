from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import  status
from .models import (
    Answer,
    Question,
    Quiz
)


class AnswerModelTestCase(TestCase):

    def setUp(self):
        self.answer_content = 'Answer is yes'
        self.answer = Answer(content=self.answer_content)

    def test_can_create_answer(self):
        old_count = Answer.objects.count()
        self.answer.save()
        new_count = Answer.objects.count()
        self.assertNotEqual(old_count, new_count)


class QuestionModelTestCase(TestCase):

    def setUp(self):
        self.answer_yes = Answer.objects.create(content='yes')
        self.answer_no = Answer.objects.create(content='no')
        self.question_content = 'Are you human?'
        self.question = Question(content=self.question_content)

    def test_can_create_question(self):
        old_count = Question.objects.count()

        self.question.correct_answer = self.answer_yes
        self.question.save()
        self.question.answers.add(self.answer_yes)
        self.question.answers.add(self.answer_no)

        new_count = Question.objects.count()
        self.assertNotEqual(old_count, new_count)


class QuizModelTestCase(TestCase):

    def setUp(self):
        self.answer_yes = Answer.objects.create(content='yes')
        self.answer_no = Answer.objects.create(content='no')

        self.question_content = 'Are you human?'
        self.question = Question(content=self.question_content)
        self.question.correct_answer = self.answer_yes
        self.question.save()
        self.question.answers.add(self.answer_yes)
        self.question.answers.add(self.answer_no)

        self.quiz_title = 'Quiz'
        self.quiz = Quiz(title='Quiz')

    def test_can_create_quiz(self):
        old_count = Quiz.objects.count()

        self.quiz.save()
        self.quiz.questions.add(self.question)

        new_count = Quiz.objects.count()

        self.assertNotEqual(old_count, new_count)


class QuizViewTestModel(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.answer1 = Answer.objects.create(content='Answer 1')
        self.answer2 = Answer.objects.create(content='Answer 2')
        self.question1 = Question.objects.create(content='Question 1', correct_answer=self.answer1)
        self.question1.answers.add(self.answer1)
        self.question1.answers.add(self.answer2)
        self.quiz = Quiz.objects.create(title='Quiz 1')
        self.quiz.questions.add(self.question1)

    def test_api_can_get_quiz_list(self):
        response = self.client.get(reverse('quiz-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_get_quiz_detail(self):
        response = self.client.get(reverse('quiz-detail', kwargs={'pk': self.quiz.pk}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)