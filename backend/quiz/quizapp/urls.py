from django.urls import path, include
from rest_framework_nested import routers

from .views import QuizViewSet

quiz_router = routers.SimpleRouter()
quiz_router.register('quiz', QuizViewSet, base_name='quiz')

urlpatterns = [
    path('', include(quiz_router.urls)),
]
