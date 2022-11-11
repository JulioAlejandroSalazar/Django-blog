from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
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
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(max_length=100, label="Name", required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(max_length=100, label="Last Name", required=False, widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class ProfileEditForm(forms.ModelForm):
    birth_date = forms.DateField(input_formats=['%d/%m/%Y', '%Y-%m-%d'], required=False, widget=forms.DateInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            #'birth_date': forms.DateInput(attrs={'class': 'form-control'}), had tu use it above, idk how to make it properly work in both ways
            'short_description': forms.TextInput(attrs={'class': 'form-control'}),
            'generic_link': forms.URLInput(attrs={'class': 'form-control'}),
            'github_link': forms.URLInput(attrs={'class': 'form-control'}),
            'instagram_link': forms.URLInput(attrs={'class': 'form-control'}),
            'facebook_link': forms.URLInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
        }


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model = User
        fields = ["old_password", "new_password1", "new_password2"]
        help_texts = {k:"" for k in fields}

