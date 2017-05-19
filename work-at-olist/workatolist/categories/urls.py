from django.conf.urls import url

from rest_framework import status
from rest_framework.response import Response

from .views import return_list

urlpatterns = [
    url(r'^/$', return_list, name='list'),
]
