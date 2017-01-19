from django.conf.urls import url

from django.http import HttpResponse

from rest_framework import status

urlpatterns = [
    url(r'^/$', lambda x: HttpResponse(status.HTTP_200_OK), name='list'),
]
