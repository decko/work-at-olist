from __future__ import unicode_literals

from django.db import models


class Channel(models.Model):
    """
    Persist a channel.
    """

    name = models.CharField('Marketplace name', max_length=100)
