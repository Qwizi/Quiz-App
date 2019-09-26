from django.urls import path, include
from rest_framework_nested import routers

from .views import (
    UserViewSet,
    QuizAnswerViewSet,
    UserQuizAnswerViewSet
)

user_router = routers.SimpleRouter()
user_router.register('user', UserViewSet, base_name='user')
user_router.register('quiz-answer', QuizAnswerViewSet, base_name='quiz-answer')

user_quiz_answer_router = routers.NestedSimpleRouter(user_router, 'user', lookup='user')
user_quiz_answer_router.register('quiz-answer', UserQuizAnswerViewSet, base_name='user-quiz-answer')

urlpatterns = [
    path('', include(user_router.urls)),
    path('', include(user_quiz_answer_router.urls))
    # path('', include(user_quiz_answer.urls))
    # path('', include(quiz_router.urls)),
    # path('', include(question_router.urls)),
    # path('', include(answer_router.urls))
]
