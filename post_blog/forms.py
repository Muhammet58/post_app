from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import post_model


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
        fields = (
            "title",
            "text",
        )
