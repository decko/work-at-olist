from django.conf.urls import url

from .views import ChannelsView

urlpatterns = [
    url(r'^channels/$', ChannelsView.as_view(), name='channels')
]
