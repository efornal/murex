from app.models import Estado, Proveedor

def states(request):
    return {'states': Estado.objects.order_by('nombre')}

def providers(request):
    return {'providers': Proveedor.objects.order_by('nombre')}

def current_state(request):
    if 'state' in request.POST:
        return {'current_state': request.POST.get('state')}
    else:
        return {'current_state': None}

def current_provider(request):
    if 'provider' in request.POST:
        return {'current_provider': request.POST.get('provider')}
    else:
        return {'current_provider': None}

