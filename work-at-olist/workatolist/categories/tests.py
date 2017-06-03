import json

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from .models import Category


class CategoriesTest(APITestCase):
    """
    Tests for Category model and endpoints
    """

    def test_categories_endpoint_returning_200_ok(self):
        """
        Test for /categories/ url return HTTP 200 ok status
        """

        url = '/categories/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_categories_namespace_returning_the_correct_url(self):
        """
        Test if 'categories' url name return '/categories/' as url
        """

        url = '/categories/'
        reversed = reverse('categories:list')

        self.assertEqual(url, reversed)

    def test_returning_a_list_from_endpoint(self):
        """
        Test returning a list from the endpoint
        """

        url = reverse('categories:list')

        response = self.client.get(url)

        self.assertIsInstance(response.data, list)

    def test_returning_a_list_with_some_categories_from_endpoint(self):
        """
        Test returning some values inside a list as response from endpoint
        request
        """

        categories = ('Games', 'Computers', 'Books')
        for category in categories:
            Category.objects.create(name=category)

        url = reverse('categories:list')

        response = self.client.get(url)

        for category in categories:
            self.assertContains(response, category, status_code=200)

    def test_returning_a_list_with_some_persisted_categories(self):
        """
        Test return all categories persisted in the database
        """

        categories = ('Games', 'Computers', 'Books', 'Power Tools')
        for category in categories:
            Category.objects.create(name=category)

        url = reverse('categories:list')

        response = self.client.get(url)

        for category in categories:
            self.assertContains(response, category, status_code=200)
