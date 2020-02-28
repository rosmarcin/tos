from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from tos_app import models, serializers
from random import randint


class TermsOfServiceViewSetTests(APITestCase):
    """
    Standard CRUD test

    """
    user = 1
    username = 'user'
    first_name = 'Jan'
    last_name = 'Kowalski'
    street = 'Aleje'
    post_code = '00-123'
    tos_version1 = 1
    tos_version2 = 2

    tos_content1 = 'tos content1'

    # Test Data Setup
    @classmethod
    def setUpTestData(cls):
        for i in range(1, 10):
            cls.usr_obj = User.objects.create_user(
                username=cls.username+str(i),
                email=cls.username+str(i)+'@localhost.net',
                password='admin123!',

            )

            cls.obj = models.TermsOfService.objects.create(
                content=cls.tos_content1
            )

    # Endpoint /tos, method GET list
    def test_tos_list(self):
        path = '/api/v1/tos/'
        response = self.client.get(reverse('tos-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Endpoint /tos, method GET detail
    def test_tos_detail(self):
        response = self.client.get(reverse('tos-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['content'], self.tos_content1)

    # Endpoint /tos, method POST - create
    # Test creation of new record
    def test_tos_create(self):
        response = self.client.post(reverse('tos-list'), {
            'content': self.tos_content1,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['content'], self.tos_content1)
        self.assertEqual(response.data['version'], '1.0')

    # Endpoint tos, method PATCH
    # test updating existing ToS record, editable constraint set on model
    def test_tos_patch(self):
        response = self.client.patch(reverse('tos-detail', kwargs={'pk': 1}), {
            'content': self.tos_content1+'modified',
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Endpoint tos, method UPDATE
    # test updating existing ToS record, editable constraint set on model
    def test_tos_put(self):
        response = self.client.put(reverse('tos-detail', kwargs={'pk': 1}), {
            'content': self.tos_content1+'modified',
            'version': '2.0',
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_tos_delete(self):
        response = self.client.delete(reverse('tos-detail', kwargs={'pk': 1}))
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class UserTermsOfServiceViewSetTests(APITestCase):
    """
    Standard CRUD test

    """
    user = 1
    username = 'user'

    tos_content = 'Sample Terms of Service'
    first_name = 'Jan'
    last_name = 'Kowalski'
    street = 'Aleje'
    post_code = '00-123'
    tos_version1 = 1
    tos_version2 = 2

    # Test Data Setup
    @classmethod
    def setUpTestData(cls):

        for i in range(1, 3):

            cls.usr_obj = User.objects.create_user(
                username=cls.username+str(i),
                email=cls.username+str(i)+'@localhost.net',
                password='admin123!',
            )

            cls.tos_obj = models.TermsOfService.objects.create(
                content=cls.tos_content+str(i)
            )

        cls.tos_user_obj = models.UserTerms.objects.create(
            first_name=cls.first_name,
            last_name=cls.last_name,
            street=cls.street,
            post_code=cls.post_code,
            tos_version=models.TermsOfService.objects.get(id=1),
            user=User.objects.get(id=1),
        )

    def test_user_tos_create(self):

        response = self.client.post(reverse('user_tos-list'), {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'street': self.street,
            'post_code': self.post_code,
            'tos_version': 1,
            'user': 1
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['first_name'], self.first_name)

    def test_user_tos_list(self):
        response = self.client.get(reverse('user_tos-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Endpoint /user_tos, method GET, format='HTML'
    # should return  HTML version of User Terms with pre-populated first_name, last_name
    # if known to the authenticated user
    # TODO user authentication

    def test_user_tos_detail(self):

        url = reverse('user_tos-get-agreement',
                      kwargs={'pk': 1})+'?format=html'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def authenticate_user(self):
        # standard authentication authenticate user
        self.user = User.objects.create_user(
            username='user10', password='admin123!')
        self.token = Token.objects.create(
            user=User.objects.get(username='user10'))
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)
