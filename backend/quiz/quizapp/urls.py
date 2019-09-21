from rest_framework import routers

from .views import UserAnswerViewSet, QuizViewSet

router = routers.SimpleRouter()
router.register('user-answer', UserAnswerViewSet)
router.register('quiz', QuizViewSet)

urlpatterns = router.urls
