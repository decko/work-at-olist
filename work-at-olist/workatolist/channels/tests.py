from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class ChannelsTest(APITestCase):
    def test_channels_endpoint_returning_200_OK(self):

        url = reverse('channels')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
