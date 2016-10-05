from django.shortcuts import render
from django.views.generic import ListView
from pure_pagination.mixins import PaginationMixin

from .models import Post


class IndexView(PaginationMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 5
    context_object_name = 'posts'