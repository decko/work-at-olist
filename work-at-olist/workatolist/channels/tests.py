from django.core.urlresolvers import resolve

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from .models import Channel


class ChannelsTest(APITestCase):
    def test_channels_endpoint_returning_200_OK(self):

        url = reverse('channels')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_channels_endpoint_use_channels_url(self):

        url = resolve('/channels/')

        self.assertEqual(url.view_name, 'channels')

    def test_channels_endpoint_return_channels_list(self):

        Channel.objects.create(name="SuperMarketplace")

        url = reverse('channels')
        response = self.client.get(url)

        self.assertContains(response, "SuperMarketplace")
