from django.conf import settings
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, TemplateView, FormView

from .forms import ContactForm
from .models import Post, JobPositions, IndexPage


class IndexView(TemplateView):
    queryset = IndexPage.objects.all().values_list(
        'description', flat=True).first()
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['index'] = self.queryset
        return context


class PostsListView(ListView):
    queryset = Post.objects.filter(publish=True).only('id',
                                                      'title',
                                                      'text'
                                                      ).order_by('-created')
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
        context['form'] = ContactForm()
        return context


class ContactView(FormView):
    form_class = ContactForm
    template_name = ''
    success_url = '/about/'

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return JsonResponse(form.errors, status=400)

    def send_message(self, form):
        """
        Sending emails
        :param form: current valid form
        """
        subject = 'Из блога'
        address = form.cleaned_data.get('email', '? - не указано')
        message = form.cleaned_data.get('message', '')
        message += '\n\n адрес отправителя: {}'.format(address)
        from_email = settings.EMAIL_HOST_USER
        to_email = settings.EMAIL_HOST_USER
        msg = EmailMessage(subject, message, from_email, to=[to_email])
        msg.send()

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        self.send_message(form)
        if self.request.is_ajax():
            data = {
                'success': "Ваше сообщение отправлено!"
            }
            return JsonResponse(data)
        else:
            return response

