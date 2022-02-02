from asyncio.windows_events import NULL
from unicodedata import name
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(models.Model):

    name = models.CharField(max_length=100)
    parent = models.IntegerField(default= NULL)
    child = models.IntegerField(default= NULL)
    def __str__(self):
        return self.name


class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name
    class MPTTMeta:
        order_insertion_by = ['name']

class Tag(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    tag_name = models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name
        





