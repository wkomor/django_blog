from django.db import models
from django_extensions.db.models import TimeStampedModel

from taggit.managers import TaggableManager


class Post(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name='Заголовок',
                             db_index=True)
    text = models.TextField(verbose_name='Текст', blank=True, null=True)

    tags = TaggableManager()
