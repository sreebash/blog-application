from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import TextInput


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='First Name',
                                 error_messages={'required': 'First Name is Required'},
                                 widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Last Name',
                                widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    username = forms.CharField(max_length=50, required=True, help_text='Username',
                               widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(max_length=255, help_text='Email',
                             widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.Field(help_text='Password',
                            widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Password'}))
    password2 = forms.Field(help_text='Retype Password',
                            widget=forms.PasswordInput(
                                attrs={'class': "form-control", 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',)

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == '':
            raise forms.ValidationError('First name is required')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name == '':
            raise forms.ValidationError('Last name is required')
        return last_name

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is not unique")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is not unique")
        return email

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data.get('confirm_password')
        original_password = self.cleaned_data.get('password', '')
        if original_password != confirm_password:
            raise forms.ValidationError("Password didn't match!")
        return confirm_password


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username', 'class': 'form-control'})
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Password', 'class': 'form-control'
        })
