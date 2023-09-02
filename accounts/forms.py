from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', help_text='')
    email = forms.CharField(widget=forms.EmailInput(), required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(), help_text='')
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(), help_text='')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']