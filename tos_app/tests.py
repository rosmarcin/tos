from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase

from tos_app import models, serializers
from random import randint


class TermsOfServiceViewSetTests(APITestCase):
    """
    Standard CRUD test

    """
    tos_content1 = 'tos content1'

    # Test Data Setup
    @classmethod
    def setUpTestData(cls):
        for i in range(1, 10):
            cls.foo = models.TermsOfService.objects.create(
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
