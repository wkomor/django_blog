from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'tags']
    readonly_fields = ['created']
