from django.contrib.auth.views import LoginView

from apps.academics.forms import EmailAuthenticationForm


class EmailLoginView(LoginView):
    form_class = EmailAuthenticationForm
    template_name = 'material/admin/auth/login.html'
