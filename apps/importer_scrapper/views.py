from datetime import datetime

from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.utils import IntegrityError

from apps.importer_scrapper.forms import ReadFileForm
from apps.importer_scrapper.tasks import validate_file_task
from apps.importer_scrapper.forms import ExternalAuthForm
from apps.students.models import Student
from utils.emails import EmailBuilder


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = "home.html"


class ExternalLoginView(FormView):
    form_class = ExternalAuthForm
    template_name = 'auth/login.html'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        user = authenticate(username=email, password=password)
        if user is not None and user.is_active:
            login(self.request, user)

            return redirect('home')

        return super().form_valid(form)


class ExternalLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect("login")


class ReadFileView(FormView):
    form_class = ReadFileForm
    template_name = 'read_file.html'
    success_url = reverse_lazy('readfile')

    def form_valid(self, form):
        file = form.cleaned_data['file']

        if self._is_extension_allowed(file):
            error_message = _("Only Excel and CSV files are allowed.")
            form.add_error('file', error_message)
            return self.form_invalid(form)

        errors, students_dict = validate_file_task(file)
        try:
            self.save_list_of_students(students_dict)
        except IntegrityError as error:
            error_message = _(f"Email or document number must be unique.")
            form.add_error('file', error_message)
            return self.form_invalid(form)

        if len(errors) > 0:
            self._show_validation_errors(errors, form)
            return self.form_invalid(form)

        if not form.errors:
            messages.success(self.request, _("Students has been saved successfully."))

        email_builder = EmailBuilder()

        for student in students_dict:
            email_builder\
                .set_template('emails/mail_template_admin.html')\
                .add_email(self.request.user.email)\
                .set_context(student)\
                .set_subject('Estudiante agregado exitosamente')\
                .send()
            email_builder\
                .set_template('emails/mail_template_student.html')\
                .add_email(self.request.user.email)\
                .add_email(student['email'])\
                .set_context(student)\
                .set_subject('Bienvenido al curso')\
                .send()

        return super().form_valid(form)

    def _show_validation_errors(self, errors: set, form):
        for error in errors:
            error_message = _(error)
            form.add_error('file', error_message)

    def _is_extension_allowed(self, file):
        allowed_extensions = ['xls', 'xlsx', 'csv']
        file_extension = self._extract_file_extension(file)
        return not any(file_extension.endswith(ext) for ext in allowed_extensions)

    def _extract_file_extension(self, file):
        return file.name.rsplit('.', 1)[-1].lower()

    def save_list_of_students(self, students_dict: list):
        date_format = "%Y-%m-%d"
        students = [
            Student(
                document_number=student['document_number'],
                first_name=student['first_name'],
                last_name=student['last_name'],
                born_date=datetime.strptime(student['born_date'], date_format).date(),
                address=student['address'],
                email=student['email'],
                phone=student['phone'],
                gender=student['gender'],
                career=student['career']
            )
            for student in students_dict
        ]
        Student.objects.bulk_create(students)

