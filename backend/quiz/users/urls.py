from django.urls import path, include
from rest_framework_nested import routers

from .views import (
    UserViewSet,
    UserQuizViewSet,
    UserQuestionViewSet,
    UserAnswerViewSet
)

user_router = routers.SimpleRouter()
user_router.register('user', UserViewSet, base_name='user')

quiz_router = routers.NestedSimpleRouter(user_router, 'user', lookup='user')
quiz_router.register('quiz', UserQuizViewSet, base_name='quiz')

question_router = routers.NestedSimpleRouter(quiz_router, 'quiz', lookup='quiz')
question_router.register('question', UserQuestionViewSet, base_name='question')

answer_router = routers.NestedSimpleRouter(question_router, 'question', lookup='question')
answer_router.register('answer', UserAnswerViewSet, base_name='answer')

urlpatterns = [
    path('', include(user_router.urls)),
    path('', include(quiz_router.urls)),
    path('', include(question_router.urls)),
    path('', include(answer_router.urls))
]
