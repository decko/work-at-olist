from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^channels/',
        include('workatolist.channels.urls', namespace='channels')),
    url(r'^categories/',
        include('workatolist.categories.urls', namespace='categories')),
]
