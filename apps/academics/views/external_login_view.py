from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login

from apps.academics.forms import ExternalAuthForm


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
