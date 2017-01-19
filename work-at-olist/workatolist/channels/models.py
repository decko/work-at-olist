from __future__ import unicode_literals

import uuid

from django.db import models


class UniqueIdentifier(models.Model):
    """
    Create a unique identifier as primary key to anyone
    who extends from this class.
    """
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)

    class Meta:
        abstract = True


class Channel(UniqueIdentifier):
    """
    Persist a channel.
    """

    name = models.CharField('Marketplace name', max_length=100)
    slug = models.SlugField('Unique marketplace name', unique=True,
                            default='unnamed')
