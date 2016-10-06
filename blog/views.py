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

    MONTH = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль",
             "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

    def get_month_name(self, number):
        if isinstance(number, int) and 0 < number <= 12:
            return self.MONTH[number-1]

    def get_month(self, data):
        data['month_from'] = self.get_month_name(data.get('month_from'))
        data['month_to'] = self.get_month_name(data.get('month_to'))
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        positions = list(JobPositions.objects.all().values())

        context['positions'] = map(self.get_month, positions)
        return context