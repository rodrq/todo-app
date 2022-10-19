from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUser(UserCreationForm):
    username = forms.CharField(min_length=3)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
