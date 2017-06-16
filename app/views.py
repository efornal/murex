from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.shortcuts import redirect
from app.models import Toner, Estado, EstadoToner, Proveedor
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import logging
from django.conf import settings
from django.utils.translation import ugettext as _
from django.utils import translation


def set_language(request, lang='es'):
    if 'lang' in request.GET:
        lang = request.GET['lang']
    translation.activate(lang)
    request.session[translation.LANGUAGE_SESSION_KEY] = lang
    logging.info("Language changed by the user to '{}'".format(lang))
    return redirect('index')


@login_required
def index(request):
    return redirect('toners_por_modelos')

def class_listings():
    return [settings.CSS_SEPARATOR_COLOR1, settings.CSS_SEPARATOR_COLOR2]

def rotate_colour(color):
    if color == class_listings()[0]:
        return class_listings()[1]
    else:
        return class_listings()[0]

def changes_models_list(toners):
    rows_of_changes = []
    model = ''
    if toners:
        model = toners[0].modelo
    color = class_listings()[1]
    for toner in toners:
        if (toner.modelo == model):
            rows_of_changes.append(color)
        else:
            color = rotate_colour(color)
            rows_of_changes.append(color)
            model = toner.modelo
    rows_of_changes.reverse()
    return rows_of_changes


def variations_models_list(toners):
    rows_of_changes = []
    model = ''
    if toners:
        model = toners[0].modelo
    for toner in toners:
        if (toner.modelo == model):
            rows_of_changes.append('')
        else:
            rows_of_changes.append(settings.CSS_SEPARATOR_NAME)
            model = toner.modelo
    rows_of_changes.reverse()
    return rows_of_changes

def changes_states_list(toners):
    rows_of_changes = []
    state = toners[0].ultimo_estado().id
    color = class_listings()[1]
    for toner in toners:
        if (toner.ultimo_estado().id == state):
            rows_of_changes.append(color)
        else:
            color = rotate_colour(color)
            rows_of_changes.append(color)
            state = toner.ultimo_estado().id
    rows_of_changes.reverse()
    return rows_of_changes


def variations_states_list(toners):
    rows_of_changes = []
    state = toners[0].ultimo_estado().id
    for toner in toners:
        if (toner.ultimo_estado().id == state):
            rows_of_changes.append('')
        else:
            rows_of_changes.append(settings.CSS_SEPARATOR_NAME)
            state = toner.ultimo_estado().id
    rows_of_changes.reverse()
    return rows_of_changes

  
@login_required
@staff_member_required
def toners_por_modelos (request):
    toners_list = Toner.por_modelos()
    paginator = Paginator(list(toners_list), settings.PAGINATE_BY_PAGE)
    page = request.GET.get('page')
    
    try:
        toners = paginator.page(page)
    except PageNotAnInteger:
        toners = paginator.page(1)
    except EmptyPage:
        toners = paginator.page(paginator.num_pages)

    context = {'toners': toners,
               'changes_class': changes_models_list(toners),
               'variations_class': variations_models_list(toners)}
    return render(request, 'toners.html', context)


@login_required
@staff_member_required
def toners_por_estados (request):
    toners_list = Toner.por_estados()
    paginator = Paginator(list(toners_list), settings.PAGINATE_BY_PAGE)
    page = request.GET.get('page')
    
    try:
        toners = paginator.page(page)
    except PageNotAnInteger:
        toners = paginator.page(1)
    except EmptyPage:
        toners = paginator.page(paginator.num_pages)

    context = {'toners': toners,
               'changes_class':changes_states_list(toners),
               'variations_class':variations_states_list(toners),}
    return render(request, 'toners.html', context)

    
@login_required
@staff_member_required
def toners(request):
    last_model = ''
    toners_list = Toner.objects.order_by('identificador','modelo')
    paginator = Paginator(toners_list, settings.PAGINATE_BY_PAGE)
    page = request.GET.get('page')
 
    try:
        toners = paginator.page(page)
    except PageNotAnInteger:
        toners = paginator.page(1)
    except EmptyPage:
        toners = paginator.page(paginator.num_pages)

    
    context = {'toners': toners, 'last_model': last_model}
    return render(request, 'toners.html', context)

@login_required
@staff_member_required
def toner_detail(request,toner_id):
    toner = Toner.objects.get(id=toner_id)
    status_list = EstadoToner.objects.filter(toner_id=toner_id).order_by('-fecha_inicio')
    paginator = Paginator(status_list, settings.PAGINATE_BY_PAGE)
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
@staff_member_required
def search(request):
    text_search = request.POST['search_field']
    toners_list = Toner.objects.filter(identificador__contains=text_search).order_by('identificador')
    paginator = Paginator(toners_list, settings.PAGINATE_BY_PAGE)
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
@staff_member_required
def logout_view(request):
    logout(request)
    return redirect('toners')


@login_required
@staff_member_required
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
        descripcion = request.POST['descripcion'] or None
        toner.definir_estado(nuevo_estado_id)
        if descripcion != toner.descripcion:
            toner.descripcion = descripcion
            toner.save(update_fields=['descripcion'])
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
                return redirect('index')
            else:
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

@login_required
@staff_member_required
def filtrar_listado (request):

    if 'state' in request.GET and request.GET.get('state'):
        toners_list = Toner.por_estado( request.GET.get('state') )

    elif 'provider' in request.GET and request.GET.get('provider'):
        toners_list = Toner.por_proveedor( request.GET.get('provider') )
    else:
        return redirect('index')

    paginator = Paginator(list(toners_list), settings.PAGINATE_BY_PAGE)
    page = request.GET.get('page')

    try:
        toners = paginator.page(page)
    except PageNotAnInteger:
        toners = paginator.page(1)
    except EmptyPage:
        toners = paginator.page(paginator.num_pages)

    context = {'toners': toners }

    return render(request, 'toners.html', context)
