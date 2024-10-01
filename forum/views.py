from django.shortcuts import render
from django.template import loader
from django.db import transaction
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def homePageView(request):
    return render(request, 'forum/index.html')

def listView(request):
    return render(request, 'forum/list.html')
