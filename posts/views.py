from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import CommentForm, PostForm
import json
from django.contrib.auth import logout


def home(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
        'user': request.user
    }
    print(request.user)
    return render(request, 'posts/posts.html', context)


def post(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=pk)
    request.session['postID'] = pk

    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'posts/post_details.html', context)


def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        request.POST._mutable = True
        request.POST['created_by'] = request.user
        request.POST._mutable = False

        form = PostForm(request.POST)
        if form.is_valid():
            print('ok')
            newPost = form.save()
            return redirect(f'/post/{newPost.id}')

    context = {
        'form': form
    }
    return render(request, 'posts/add_post.html', context)


def createComment(request, pk):
    postID = request.session['postID']
    post = Post.objects.get(id=postID)

    if request.method == 'POST':
        request.POST._mutable = True
        request.POST['post'] = post
        request.POST['created_by'] = request.user
        request.POST._mutable = False

        form = CommentForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()

    form = CommentForm()
    context = {'form': form}

    return render(request, 'posts/add_comment.html', context)
