from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField("Category", max_length=50, blank=True)
