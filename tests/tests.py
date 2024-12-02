import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_manager.settings")
django.setup()

import pytest
from django.contrib.auth.models import User
from api.models import Task
from rest_framework.test import APIClient
from rest_framework import status




@pytest.fixture
def create_user():
    return User.objects.create_user(username="test_user", password="password_test")

@pytest.fixture
def create_task():
    return Task.objects.create(user=create_user,title="title_test", description="description_test", status="concluido")

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_create_task(api_client, create_user):
    user = create_user
    api_client.force_authenticate(user = user)
    response = api_client.post("/api/tasks/", {
        "user_owner": user.id,
        "title": "test_title",
        "description": "test_description"
    })
    print("---------------------------------")
    print(response.data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["title"] == "test_title"