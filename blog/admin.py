from django import forms
from django.contrib import admin
from .models import Post, JobPositions, IndexPage
from ckeditor.widgets import CKEditorWidget


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['title', 'text', 'tags']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    readonly_fields = ['created']\


@admin.register(JobPositions)
class JobAdmin(admin.ModelAdmin):
    pass


@admin.register(IndexPage)
class IndexAdmin(admin.ModelAdmin):
    pass
