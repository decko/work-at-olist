from django.conf.urls import url
from django.contrib import admin

from workatolist.channels.views import ChannelsView
from workatolist.channels.views import ChannelsDetailView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^channels/(?P<uid>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})', ChannelsDetailView.as_view(), name='channels-detail'),
    url(r'^channels/$', ChannelsView.as_view(), name='channels'),

]
