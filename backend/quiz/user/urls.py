from rest_framework import routers

from .views import UserViewSet

router = routers.SimpleRouter()
router.register('user', UserViewSet)

urlpatterns = router.urls
