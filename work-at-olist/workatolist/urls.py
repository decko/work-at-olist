from django.conf.urls import url
from django.contrib import admin

from workatolist.channels.views import ChannelsView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^channels/$', ChannelsView.as_view(), name='channels'),

]
