from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
from blog_app.models import Post
from .forms import *
from .models import *



def login_view(request):
    if request.method == "POST":        
        username = request.POST['username']
        password = request.POST['password']        
        if User.objects.filter(username=username).exists() == False:
            messages.error(request, 'User does not exist')
            return redirect('login_view') 
        elif authenticate(request, username = username, password = password) == None:
            messages.error(request, 'Incorrect password')
            return redirect('login_view')       
        else:
            user = authenticate(request, username = username, password = password)        
            login(request, user)    
            messages.success(request, f'Good to see you again, {username}!')
            return redirect('home')

    else:
        context = {
            "form" : AuthenticationForm()
        }
        return render(request, 'user_app/login.html', context)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password1"]
        #checking if the user exists, case insensitive
        if User.objects.filter(username__iexact=username).exists():
            messages.error(request, 'That username already exists')
            return redirect('register')
        else:
            if form.is_valid():         
                form.save()
                user = authenticate(request, username = username, password = password)
                login(request, user)
                ruser = request.user
                Profile.objects.get_or_create(user = ruser)
                messages.success(request, f'Welcome for the first time {username}, make yourself at home')
                return redirect('home')
            else:             
                messages.error(request, 'Passwords did not match')
                return redirect('register')
    
    else:
        context = {
            "form" : UserRegisterForm()
        }
        return render(request, 'user_app/register.html', context)


class Logout(LoginRequiredMixin, LogoutView):
    posts = Post.objects.order_by('-date')
    last_post = Post.objects.latest('date')
    template_name = "blog_app/home.html"
    extra_context = {
        "message" : "You've successfully Logout",
        "posts" : posts,
        "last_post" : last_post,
        }


@login_required
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
            messages.success(request, 'Profile edited successfully')
            return redirect("my_profile")
        context = {
            "error" : "Invalid data",
            "form_user" : form_user,
            "form_profile" : form_profile,
        }
        return render(request, 'blog_app/home.html', context)
        
    else:
        player, created = Profile.objects.get_or_create(user = user)
        context = {
            'form_user' : UserEditForm(instance = user),
            'form_profile' : ProfileEditForm(instance = user.profile),
        }
        return render(request, "user_app/edit_profile.html", context)


@login_required
def change_password(request):
    if request.method == "POST":
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully')
            return redirect("my_profile")
        messages.error(request, "Password did not match")
        return redirect("change_password")

    else:
        context = {
            "form" : UserPasswordChangeForm(request.user)
        }
        return render(request, "user_app/change_password.html", context)


def get_avatar(request):
    pass