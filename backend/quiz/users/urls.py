from django.urls import path, include
from rest_framework_nested import routers

from .views import (
    UserViewSet,
)

router = routers.SimpleRouter()
router.register('user', UserViewSet, base_name='user')

urlpatterns = [
    path('', include(router.urls)),
]
