from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import *
from .models import *
from user_app.models import Profile
from django.utils import timezone



def home(request):
    posts = Post.objects.all().order_by('-date')
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    last_post = Post.objects.latest('date')
    if not posts.exists():
        return render(request, 'blog_app/home.html')
    context = {
        'posts' : page_obj,
        'last_post' : last_post,
    }
    return render(request, 'blog_app/home.html', context)


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
            count.save()
            messages.success(request, 'Publication posted successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid data')
            return redirect('create_post')

    context = {
        'form' : PostForm()
    }
    return render(request, 'blog_app/create_post.html', context)


def get_post(request, id):
    post = Post.objects.get(id=id)
    context = {
        "post" : post
    }
    return render(request, 'blog_app/get_post.html', context)


@login_required
def edit_post(request, id):
    user = request.user
    post = Post.objects.get(id=id)
    if request.user == post.author:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = user
                instance.is_edited = True
                instance.date = str(timezone.now())
                instance.save()
                messages.success(request, 'Publication edited successfully!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid data')
                return redirect('edit_post')

        context = {
            'form' : PostForm(instance=post),
            'post' : post,
        }
        return render(request, 'blog_app/edit_post.html', context)
    messages.error(request, 'user not authorized to do that')
    return redirect('home')


@login_required
def delete_post(request, id):
    post = Post.objects.get(id=id)
    user = request.user
    if request.method == 'POST':
        post.delete()
        count = Profile.objects.get(user=user)
        count.post_count -= 1
        count.save()
        messages.success(request, 'Publication deleted successfully!')
        return redirect('home')

    context = {
        'post' : post,
        'message' : 'Are your sure you want to delete this post?',
    }
    return render(request, 'blog_app/delete_post.html', context)


def posts_by_author(request, id):
    posts = Post.objects.filter(author=id).order_by('-date')
    user = User.objects.get(id=id)
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts' : page_obj,
        'user' : user,
    }
    return render(request, 'blog_app/posts_by_author.html', context)


def about(request):
    return render(request, 'blog_app/about.html')