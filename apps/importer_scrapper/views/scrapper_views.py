from pprint import pprint

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.urls import reverse_lazy

from apps.importer_scrapper.forms import ScrapperForm
from apps.importer_scrapper.tasks import (
    make_scrapper,
    save_courses_into_database,
)
from utils.emails import EmailBuilder

from pprint import pprint

class ScrapperView(LoginRequiredMixin, FormView):
    form_class = ScrapperForm
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'scrapper.html'
    success_url = reverse_lazy('scrapper')

    def form_valid(self, form):
        topic = form.cleaned_data['topic']

        courses_task = make_scrapper.delay(topic)

        courses = courses_task.get()

        if(len(courses) == 0):
            error_message = _(f"There are no such courses on the website.")
            form.add_error('topic', error_message)
            return self.form_invalid(form)

        save_courses_into_database.delay(courses)

        if len(courses) > 0 and not form.errors:
            messages.success(self.request,
                _("Courses has been saved successfully"))

        email_builder = EmailBuilder()

        email_builder\
                .set_template('emails/mail_template_admin_scrapper.html')\
                .add_email(self.request.user.email)\
                .set_context({"courses": courses})\
                .set_subject(_('Cursos agregados exitosamente'))\
                .send()

        return super().form_valid(form)


