from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *



def login_view(request):
    pass


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("username")
            form.save()
            context = {
                "message" : f"Welcome, {user}!",
                "form" : form,
            }
            return render(request, 'blog_app/home.html', context)
        context = {
            "error" : "Invalid data",
            "form" : form,
        }
        return render(request, 'user_app/register.html', context)
    
    else:
        context = {
            "form" : UserRegisterForm()
        }
        return render(request, 'user_app/register.html', context)


class Logout(LoginRequiredMixin, LogoutView):
    template_name = "blog_app/home.html"
    extra_context = {"message" : "You've successfully Logout"}


def profile(request):
    pass


def profile_edit(request):
    pass


def get_avatar(request):
    pass