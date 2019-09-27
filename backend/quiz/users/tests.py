from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from users.models import User, UserAnswer
from quizapp.models import Answer, Question, Quiz

class UserModelTestCase(TestCase):

    def setUp(self):
        self.user_name = "User 1"
        self.user = User(name=self.user_name)

    def test_can_create_user(self):
        old_count = User.objects.count()
        self.user.save()
        new_count = User.objects.count()
        self.assertNotEqual(old_count, new_count)


class UserAnswerModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(name='User 1')
        self.answer = Answer.objects.create(content='yes')
        self.question = Question.objects.create(
            content='Are u human?',
            correct_answer=self.answer
        )
        self.question.answers.add(self.answer)
        self.quiz = Quiz.objects.create(title='Test Quiz')
        self.quiz.questions.add(self.question)

        self.user_answer = UserAnswer(
            user=self.user,
            quiz=self.quiz,
            question=self.question,
            answer=self.answer
        )

    def test_can_create_user_answer(self):
        old_count = UserAnswer.objects.count()
        self.user_answer.save()
        new_count = UserAnswer.objects.count()
        self.assertNotEqual(old_count, new_count)


class UserViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user_data = {'name': 'User 1'}
        self.response = self.client.post(
            reverse('user-list'),
            self.user_data,
            format='json'
        )

    def test_api_can_create_user(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_user_list(self):
        userlist = User.objects.all()
        response = self.client.get(
            reverse('user-list'),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_get_user(self):
        user = User.objects.get()
        response = self.client.get(
            reverse('user-detail', kwargs={'pk': user.id}),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, user)


class QuizAnswerViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user_quiz_answer_data = {
            'user': 1,
            'quiz': 1,
            'question': 1,
            'answer': 1
        }
        self.user_quiz_answer_multiple_data = [
            {
                'user': 1,
                'quiz': 1,
                'question': 1,
                'answer': 1
            },
            {
                'user': 2,
                'quiz': 2,
                'question': 2,
                'answer': 2
            }
        ]
        self.response = self.client.post(reverse('quiz-answer-list'), format='json')
        self.response_multi = self.client.post(reverse('quiz-answer-list'), format='json')

    def test_api_can_create_user_quiz_answer(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_multiple_create_user_quiz_answer(self):
        self.assertEqual(self.response_multi.status_code, status.HTTP_201_CREATED)


class UserQuizAnswerViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(name='User 1')

        self.answer = Answer.objects.create(content='yes')
        self.question = Question.objects.create(
            content='Are u human?',
            correct_answer=self.answer
        )
        self.question.answers.add(self.answer)
        self.quiz = Quiz.objects.create(title='Test Quiz')
        self.quiz.questions.add(self.question)

        self.quiz_answer_data = {
            'user': self.user.pk,
            'quiz': self.quiz.pk,
            'question': self.question.pk,
            'answer': self.answer.pk
        }
        self.response = self.client.post(reverse('quiz-answer-list'), format='json')

    def test_api_can_get_user_quiz_answer_list(self):
        response = self.client.get(
            reverse(
                'user-quiz-answer-list',
                kwargs={'user_pk': self.user.pk}
            ), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_get_user_quiz_answer_questions(self):
        response = self.client.get(
            reverse(
                'user-quiz-answer-detail',
                kwargs={'user_pk': self.user.pk, 'pk': self.quiz.pk}
            ), format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
