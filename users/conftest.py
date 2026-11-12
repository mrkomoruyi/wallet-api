import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def get_users_list_response(client):
    return client.get(reverse('users-list'))


@pytest.fixture
def post_users_list_response(client):
    return client.post(
        reverse('users-list'),
        {'username': 'a', 'email': 'a@domain.com', 'password': 'testpass123'},
    )
