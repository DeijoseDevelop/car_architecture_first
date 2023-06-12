from django import forms
from django.utils.translation import gettext_lazy as _


class ReadFileForm(forms.Form):
    file = forms.FileField(
        label=_("File"),
        widget=forms.FileInput(
            attrs={"class": 'form-control'},
        ),
    )


