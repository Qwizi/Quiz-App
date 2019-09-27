from django.urls import path, include
from rest_framework_nested import routers

from .views import (
    UserViewSet,
    QuizAnswerViewSet,
    UserQuizAnswerViewSet,
    TopUserViewSet
)

router = routers.SimpleRouter()
router.register('user', UserViewSet, base_name='user')
router.register('quiz-answer', QuizAnswerViewSet, base_name='quiz-answer')
router.register('top', TopUserViewSet, base_name='top')


user_quiz_answer_router = routers.NestedSimpleRouter(router, 'user', lookup='user')
user_quiz_answer_router.register('quiz-answer', UserQuizAnswerViewSet, base_name='user-quiz-answer')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(user_quiz_answer_router.urls))
]
