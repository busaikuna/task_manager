from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, TaskViewSet, ListUserTasks
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router.register(r"users", UserViewSet)
router.register(r"tasks", TaskViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("token", obtain_auth_token),
    path("users/<int:pk>/tasks", ListUserTasks.as_view())
]