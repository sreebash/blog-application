from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import TextInput


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True,
                                 widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, required=True,
                                widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    username = forms.CharField(max_length=50, required=True,
                               widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(max_length=255, widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.Field(
        widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Password'}))
    password2 = forms.Field(
        widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',)
