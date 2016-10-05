from django.views.generic import ListView, DetailView
from pure_pagination.mixins import PaginationMixin

from .models import Post


class IndexView(PaginationMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 5
    context_object_name = 'posts'


class PostView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'