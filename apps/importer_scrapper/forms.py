from django import forms
from django.utils.translation import gettext_lazy as _

from apps.importer_scrapper.constants import TOPICS


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


class ReadFileForm(forms.Form):
    file = forms.FileField(
        label=_("File"),
        widget=forms.FileInput(
            attrs={"class": 'form-control'},
        ),
    )


class ScrapperForm(forms.Form):
    topic = forms.CharField(
        label=_("Search topic"),
        widget=forms.TextInput(
            attrs={"class": 'form-control'},
        )
    )

