from django.views.generic import ListView, DetailView, TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, JobPositions, IndexPage


class IndexView(ListView):
    queryset = IndexPage.objects.all().values_list(
                'description', flat=True).first()
    template_name = 'blog/index.html'
    context_object_name = 'index'


class PostsListView(ListView):
    queryset = Post.objects.all().values().order_by('-created')
    template_name = 'blog/posts.html'
    paginate_by = 5
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.queryset, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            context['posts'] = paginator.page(page)
        except PageNotAnInteger:
            context['posts'] = paginator.page(1)
        except EmptyPage:
            context['posts'] = paginator.page(paginator.num_pages)
        return context


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
            return self.MONTH[number - 1]

    def get_month(self, data):
        data['month_from'] = self.get_month_name(data.get('month_from'))
        data['month_to'] = self.get_month_name(data.get('month_to'))
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        positions = list(JobPositions.objects.all().values())

        context['positions'] = map(self.get_month, positions)
        return context
