from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from pytest import mark


@mark.django_db
def test_anonymous_user_can_create_user():
    client = APIClient()
    url = reverse('users-list')
    response = client.post(url, {'username': 'a', 'email': 'a@domain.com', 'password': 'testpass123'})

    assert response.status_code == status.HTTP_201_CREATED
