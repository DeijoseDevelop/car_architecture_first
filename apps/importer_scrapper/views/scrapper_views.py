from pprint import pprint

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.utils import IntegrityError

from apps.importer_scrapper.forms import ScrapperForm
from apps.courses.models import Course
from apps.importer_scrapper.tasks import make_scrapper
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

        pprint(f"Courses: {courses}")
        errors = []
        try:
            self.save_list_of_courses(errors, courses)
        except IntegrityError:
            error_message = _(f"Course Name must be unique.")
            form.add_error('topic', error_message)
            return self.form_invalid(form)

        if len(errors) > 0:
            messages.warning(self.request,
                _("Have been saved with some deleted scrapp courses."))

        if len(courses) > 0 and not form.errors and len(errors) == 0:
            messages.success(self.request,
                _("Courses has been saved successfully"))

        email_builder = EmailBuilder()

        email_builder\
                .set_template('emails/mail_template_admin_scrapper.html')\
                .add_email(self.request.user.email)\
                .set_context({"courses": courses})\
                .set_subject('Cursos agregados exitosamente')\
                .send()

        return super().form_valid(form)

    def save_list_of_courses(self, errors: list, courses_dict: list):
        date_format = "%Y-%m-%d"
        for course in courses_dict:
            try:
                course_instance = Course(
                    name=course['name'],
                    description=course['description']
                )
                course_instance.save()
            except IntegrityError as error:
                errors.append(error)
                continue

