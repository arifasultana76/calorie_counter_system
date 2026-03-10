from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,  PasswordChangeForm
from .models import *


class RegisterForm(UserCreationForm):
    class Meta:
        model = AuthUserModel
        fields = ['username', 'password1', 'password2', 'gender', 'age', 'weight', 'height']
        error_messages = {
            'username': {
                'unique': "This username already exists.",

            },
        }


class LoginForm(AuthenticationForm):
    pass


class CalorieForm(forms.ModelForm):
    class Meta:
        model = CalorieEntryModel
        fields = ['item_name', 'calories_consumed']
        

