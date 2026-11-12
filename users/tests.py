from django.urls import reverse
from pytest import mark
from rest_framework import status
from rest_framework.test import APIClient

from .models import User


def test_users_url_exists_at_correct_location(client):
    response = client.get('/api/v1/users/')
    assert response.status_code != status.HTTP_404_NOT_FOUND


def test_users_url_available_by_name(get_users_list_response):
    assert get_users_list_response.status_code != status.HTTP_404_NOT_FOUND


def test_get_users_list_requires_authentication():
    url = reverse('users-list')
    response = APIClient().get(url)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@mark.django_db
def test_anonymous_user_can_create_user(post_users_list_response):
    assert post_users_list_response.status_code == status.HTTP_201_CREATED


@mark.django_db
def test_user_creation_should_hash_password_for_save(post_users_list_response):
    user = User.objects.get(pk=post_users_list_response.data.get('id'))
    assert user.password != 'testpass123'
