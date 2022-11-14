from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import *
from user_app.models import Profile



def home(request):
    return render(request, 'blog_app/home.html')


@login_required
def create_post(request):
    if request.method == "POST":
        user = request.user
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = user
            instance.save()
            count = Profile.objects.get(user=user)
            count.post_count += 1
            messages.success(request, 'Publication posted successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid data')
            return redirect('create_post')

    context = {
        'form' : PostForm()
    }
    return render(request, 'blog_app/create_post.html', context)