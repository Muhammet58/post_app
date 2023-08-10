from django import forms
from .models import post_model
from django.contrib.auth.models import User


class post_model_form(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), label="BAŞLIK :"
    )
    text = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control textarea"}),
        label="İÇERİK :",
    )

    class Meta:
        model = post_model
        fields = ("title", "text")
