from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, TaskViewSet
from django.urls import path, include

router = DefaultRouter()

router.register(r"users", UserViewSet)
router.register(r"tasks", TaskViewSet)

urlpatterns = [
    path("api/", include(router.urls))
]