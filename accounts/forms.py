# Django Imports
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password")
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Username",
                    "type": "text",
                }
            ),
            "password": forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter password",
                    "type": "password",
                }
            ),
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Input email address",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Input password"}
        )
    )
