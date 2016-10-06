from django.db import models
from django_extensions.db.models import TimeStampedModel

from taggit.managers import TaggableManager


class Post(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name='Заголовок',
                             db_index=True)
    text = models.TextField(verbose_name='Текст', blank=True, null=True)

    tags = TaggableManager()

    def __str__(self):
        return self.title


class JobPositions(models.Model):
    title = models.CharField(max_length=1024, verbose_name='Организация')
    description = models.TextField(verbose_name='Описание')
    month_from = models.PositiveSmallIntegerField()
    month_to = models.PositiveSmallIntegerField(blank=True, null=True)
    year_from = models.PositiveIntegerField()
    year_to = models.PositiveIntegerField(blank=True, null=True)
    order = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title[:15]


class IndexPage(models.Model):
    description = models.TextField()