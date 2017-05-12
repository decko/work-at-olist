from django.conf.urls import url

from .views import ChannelsView
from .views import ChannelsDetailView

urlpatterns = [
    url(r'^/$', ChannelsView.as_view(), name='list'),
    url(r'^channels/(?P<uid>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})', ChannelsDetailView.as_view(), name='detail'),
]
