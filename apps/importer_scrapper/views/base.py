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

from apps.importer_scrapper.forms import ExternalAuthForm


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


