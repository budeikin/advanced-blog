import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from datetime import datetime
from accounts.models import User,Profile


@pytest.fixture
def api_client():
    client = APIClient()
    return client

@pytest.fixture
def user_example():
    user = User.objects.create_user(email='test@test.com',password='a/@1234567',is_verified=True)
    return user

@pytest.mark.django_db
class TestPostApi:

    def test_get_post_reponse_200_status(self,api_client):
        url  = reverse('blog:api-v1:post-list')
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_post_response_201_status(self,api_client,user_example):
        url  = reverse('blog:api-v1:post-list')
        data = {
            "title":"test",
            "content":"test",
            "status":True,
            "publishes_date":datetime.now()
        }
        user = user_example
        api_client.force_login(user=user)
        response = api_client.post(url,data)
        assert response.status_code == 201

