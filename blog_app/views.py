from turtle import home
from django.shortcuts import render



def home(request):
    return render(request, 'blog_app/home.html')