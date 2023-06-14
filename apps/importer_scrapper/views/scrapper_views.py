from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.utils import IntegrityError

from apps.importer_scrapper.forms import ScrapperForm
from utils.scrappers import DataMiner


class ScrapperView(LoginRequiredMixin, FormView):
    form_class = ScrapperForm
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'external_form.html'
    success_url = reverse_lazy('scrapper')

    def form_valid(self, form):
        topic = form.cleaned_data['topic']
        page = form.cleaned_data['page']

        print(topic)
        print(page)

        scrapper = DataMiner()
        course_names = scrapper.get_course_name(topic)
        print(f"Course names: {course_names}")

        return super().form_valid(form)
