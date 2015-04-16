from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from app.models import Toner, Estado, EstadoToner
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import transaction

@login_required
def index(request):
    return redirect('toners')


@login_required
def toners(request):
    toners_list = Toner.objects.order_by('identificador')
    paginator = Paginator(toners_list, 10)
    page = request.GET.get('page')
    try:
        toners = paginator.page(page)
    except PageNotAnInteger:
        toners = paginator.page(1)
    except EmptyPage:
        toners = paginator.page(paginator.num_pages)

    context = {'toners': toners}
    return render(request, 'toners.html', context)

@login_required
def toner_detail(request,toner_id):
    toner = Toner.objects.get(id=toner_id)
    status_list = EstadoToner.objects.filter(toner_id=toner_id).order_by('-fecha_inicio')
    paginator = Paginator(status_list, 10)
    page = request.GET.get('page')

    try:
        status = paginator.page(page)
    except PageNotAnInteger:
        status = paginator.page(1)
    except EmptyPage:
        status = paginator.page(paginator.num_pages)

    first = status[0]
    context = {'status': status, 'toner_name': toner.identificador, 'first': first}

    return render(request, 'toner_detail.html', context)


@login_required
def search(request):
    text_search = request.POST['search_field']
    toners_list = Toner.objects.filter(identificador__contains=text_search).order_by('identificador')
    paginator = Paginator(toners_list, 3)
    page = request.GET.get('page')
    try:
        toners = paginator.page(page)
    except PageNotAnInteger:
        toners = paginator.page(1)
    except EmptyPage:
        toners = paginator.page(paginator.num_pages)

    context = {'toners': toners, 'text_search': text_search }
    return render(request, 'toners.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('toners')


@login_required
@transaction.commit_on_success
def toner(request, toner_id):
    if request.method == 'GET':
        toner = Toner.objects.get(id=toner_id)
        estados = Estado.objects.order_by('nombre')
        estado_actual = toner.estado_actual()
        return render(request, 'toner.html', {'toner': toner,
                                              'estados': estados,
                                              'estado_actual': estado_actual})
    elif request.method == 'POST':
        toner = Toner.objects.get(id=toner_id)
        nuevo_estado_id = request.POST['estado_id'] or None
        if 'recargado' in request.POST and request.POST['recargado']:
            fue_recargado = True
        else:
            fue_recargado = False
        toner.definir_estado(nuevo_estado_id, fue_recargado)
        return redirect('toners')
    raise Http404
      

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

