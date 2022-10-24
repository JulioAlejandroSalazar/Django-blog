from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}


class UserEditForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, label="Name", required=False)
    last_lame = forms.CharField(max_length=100, label="Last Name", required=False)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class ProfileEditForm(forms.ModelForm):
    bio = forms.TextInput()

    class Meta:
        model = Profile
        fields = ["bio"]
