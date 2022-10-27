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
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(max_length=100, label="Name", required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(max_length=100, label="Last Name", required=False, widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class ProfileEditForm(forms.ModelForm):
    phone = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
    country = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
    birth_date = forms.DateField(required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
    short_description = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
    generic_link = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
    github_link = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
    instagram_link = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
    facebook_link = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
    bio = forms.TextInput()

    class Meta:
        model = Profile
        fields = ['phone', 'country', 'birth_date', 'short_description', 'generic_link', 'github_link', 'instagram_link', 'facebook_link', 'bio']
