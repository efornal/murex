from app.models import Estado, Proveedor

def defaults(request):
    states = Estado.objects.order_by('nombre')
    providers = Proveedor.objects.order_by('nombre')
    current_state = ''
    current_provider = ''
    
    if 'state' in request.GET:
        current_state = request.GET['state']
    if 'provider' in request.GET:
        current_provider = request.GET['provider']

    return { 'states': states,
             'providers': providers,
             'current_provider': current_provider,
             'current_state': current_state,}
