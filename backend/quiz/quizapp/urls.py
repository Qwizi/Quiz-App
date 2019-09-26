from django.urls import path, include
from rest_framework_nested import routers

from .views import (
    QuizViewSet,
    # QuestionViewSet,
    # AnswerViewSet
)

quiz_router = routers.SimpleRouter()
quiz_router.register('quiz', QuizViewSet, base_name='quiz')
"""
question_router = routers.NestedSimpleRouter(quiz_router, 'quiz', lookup='quiz')
question_router.register('question', QuestionViewSet, base_name='question')

answer_router = routers.NestedSimpleRouter(question_router, 'question', lookup='question')
answer_router.register('answer', AnswerViewSet, base_name='answer')

"""
urlpatterns = [
    path('', include(quiz_router.urls)),
    # path('', include(question_router.urls)),
    # path('', include(answer_router.urls))
]
