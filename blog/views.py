from django.views.generic import ListView, DetailView, TemplateView
from pure_pagination.mixins import PaginationMixin

from .models import Post, JobPositions


class IndexView(PaginationMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 5
    context_object_name = 'posts'


class PostView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'


class AboutView(TemplateView):
    template_name = 'blog/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['positions'] = JobPositions.objects.all()
        return context