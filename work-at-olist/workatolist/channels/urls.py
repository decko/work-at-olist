from django.conf.urls import url

from .views import ChannelsView

urlpatterns = [
    url(r'^/$', ChannelsView.as_view(), name='list')
]
