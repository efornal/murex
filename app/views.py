from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
    return HttpResponse("Hello, world.")

#def login(request):
#        return HttpResponse("login")


def login(request):
    template_response = views.login(request)
    # Do something with `template_response`
    return template_response
