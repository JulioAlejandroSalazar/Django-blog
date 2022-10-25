from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Good to see you again, {username}!')
            return redirect('home')
        context = {
            'error' : 'Username or password incorrect',
            'form' : form,
        }
        return render(request, 'user_app/login.html', context)

    else:
        context = {
            "form" : AuthenticationForm()
        }
        return render(request, 'user_app/login.html', context)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            form.save()
            user = authenticate(request, username = username, password = password)
            login(request, user)
            ruser = request.user
            player, created = Profile.objects.get_or_create(user = ruser)
            messages.success(request, f'Welcome for the first time {username}, make yourself at home')
            return redirect('home')         
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


def my_profile(request):
    user = request.user
    context = {
        "user" : user
    }
    return render(request, "user_app/profile.html", context)


def unaffiliated_profile(request, username):
    user = User.objects.get(username=username)
    context = {
        "user" : user,
        "username" : username,
    }
    return render(request, "user_app/profile.html", context)


def profile_all(request):
    users = User.objects.all()
    context = {
        "users" : users
    }
    return render(request, "user_app/profile_all.html", context)


@login_required
def profile_edit(request):
    user = request.user
    if request.method == "POST":
        form_user = UserEditForm(request.POST, instance = user)
        form_profile = ProfileEditForm(request.POST, request.FILES, instance = user.profile)
        if form_user.is_valid() and form_profile.is_valid():
            form_user.save()
            form_profile.save()
            messages.success(request, "Your profile has been updated!")
            return redirect("home")
        context = {
            "error" : "Invalid data",
            "form_user" : form_user,
            "form_profile" : form_profile,
        }
        return render(request, 'user_app/home.html', context)
        
    else:
        player, created = Profile.objects.get_or_create(user = user)
        context = {
            'form_user' : UserEditForm(instance = user),
            'form_profile' : ProfileEditForm(instance = user.profile),
        }
        return render(request, "user_app/edit_profile.html", context)


def get_avatar(request):
    pass