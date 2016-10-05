from django.contrib import admin
from .models import Post, JobPositions, IndexPage


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'tags']
    readonly_fields = ['created']\


@admin.register(JobPositions)
class JobAdmin(admin.ModelAdmin):
    pass


@admin.register(IndexPage)
class IndexAdmin(admin.ModelAdmin):
    pass
