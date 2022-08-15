from django import forms
from .models import Dweet


class DweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,  # don't want empty tweet
        widget=forms.widgets.Textarea(
            attrs={     # like CSS style in html code
                "placeholder": "Dweet something...",
                "class": "textarea is-success is-medium"
            }
        ),
        label="",   # delete the text lingering in front of the form
    )

    class Meta:
        model = Dweet
        exclude = ("user",)
