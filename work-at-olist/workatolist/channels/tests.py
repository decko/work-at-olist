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

    def test_returning_a_channel_from_endpoint(self):

        channel = Channel.objects.create(name="SuperMarketplace")

        url = reverse('channels-detail', kwargs={'uid': channel.uid})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_return_channel_name_and_uid(self):

        channel = Channel.objects.create(name="SuperMarketplace")

        url = reverse('channels-detail', kwargs={'uid': channel.uid})
        response = self.client.get(url)

        self.assertContains(response, channel.uid)
        self.assertContains(response, channel.name)

    def test_return_a_channel_using_slugs(self):

        channel = Channel.objects.create(name="SuperMarketplace")

        url = reverse('channels-slug-detail', kwargs={'slug': channel.slug})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_return_404_channel_not_found(self):

        import uuid
        fake_uid = uuid.uuid4()

        Channel.objects.create(name="SuperMarketplace")

        url = reverse('channels-detail', kwargs={'uid': fake_uid})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
