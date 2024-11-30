from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, TaskViewSet
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router.register(r"users", UserViewSet)
router.register(r"tasks", TaskViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/token", obtain_auth_token)
]