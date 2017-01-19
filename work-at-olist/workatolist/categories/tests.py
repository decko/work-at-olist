from rest_framework import status
from rest_framework.test import APITestCase


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
