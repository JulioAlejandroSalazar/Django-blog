from django import forms
from .models import *



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'post_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }