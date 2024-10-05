from django.shortcuts import render
from django.template import loader
from django.db import transaction
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def homePageView(request):
    return render(request, 'forum/index.html')

def profileView(request, username):
    return render(request, 'forum/user.html')

def postsView(request, username):
    return render(request, 'forum/posts.html')

def privatePostsView(request,username):
    return render(request, 'forum/private-posts.html')
