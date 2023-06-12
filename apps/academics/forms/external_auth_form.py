from django import forms
from django.utils.translation import gettext_lazy as _


class ExternalAuthForm(forms.Form):

    email = forms.EmailField(
        label=_("Email"),
        widget=forms.TextInput(
            attrs={
                "class": 'form-control',
                "placeholder": _("Enter your email address"),
            },
        )
    )

    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": 'form-control',
                "autocomplete": "current-password",
                "placeholder": _("Enter your password"),
            },
        )
    )
