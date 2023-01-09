from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField(label="email", required=True)
    phone_no = forms.CharField(max_length=255)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone_no', 'password')


class LoginForm(forms.ModelForm):
    email = forms.CharField(label='Email', max_length=255)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')
