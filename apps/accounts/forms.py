from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'password', 'email']


class UserFormChangeInformation(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        exclude = ['user']