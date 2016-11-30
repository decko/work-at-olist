from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Channel


class ChannelsView(APIView):

    def get(self, request):
        channels = [
            {
                'uid': channel.uid,
                'name': channel.name
            }
            for channel in Channel.objects.all()
        ]
        return Response(channels)


class ChannelsDetailView(APIView):

    def get(self, request, uid):
        channel = get_object_or_404(Channel, uid=uid)

        return Response((channel.uid, channel.name))
