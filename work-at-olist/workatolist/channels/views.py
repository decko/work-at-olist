from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Channel


class ChannelsView(APIView):

    def get(self, request):
        channels = [channel.name for channel in Channel.objects.all()]
        return Response(channels)
