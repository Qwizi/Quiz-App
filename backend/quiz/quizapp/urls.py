from rest_framework import routers

from .views import UserAnswerViewSet, QuizViewSet

router = routers.SimpleRouter()
router.register('user-answers', UserAnswerViewSet)
router.register('quizs', QuizViewSet)

urlpatterns = router.urls
