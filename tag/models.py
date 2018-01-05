"""Tags model."""
from django.db import models


class TagManager(models.Manager):
    """Tag manager"""

    def count_by_name(self, name):
        count = Tag.objects.filter(name=name).count()
        return count


class Tag(models.Model):
    """Tag model"""
    name = models.CharField(max_length=60, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = TagManager()

    def __str__(self):
        return self.name
