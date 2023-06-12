from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin


class ExternalLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect("login")