from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from app.models import Toner
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def index(request):
    return redirect('toners')


@login_required
def toners(request):
    toners_list = Toner.objects.order_by('identificador')
    paginator = Paginator(toners_list, 3)
    page = request.GET.get('page')
    try:
        toners = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        toners = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        toners = paginator.page(paginator.num_pages)

    context = {'toners': toners}
    return render(request, 'toners.html', context)

@login_required
def search(request):
    text_search = request.POST['search_field']
    toners_list = Toner.objects.filter(identificador=text_search).order_by('identificador')
    paginator = Paginator(toners_list, 3)
    page = request.GET.get('page')
    try:
        toners = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        toners = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        toners = paginator.page(paginator.num_pages)

    context = {'toners': toners}
    return render(request, 'toners.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('toners')


@login_required
def toner(request, toner_id):
    toner = Toner.objects.get(id=toner_id)
    return render(request, 'toner.html', {'toner': toner})



def login_view(request):
    if request.POST.get('username') and request.POST.get('password'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('toners')
            else:
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

