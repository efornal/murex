from app.models import Estado, Proveedor

def defaults(request):
    states = Estado.objects.order_by('nombre')
    providers = Proveedor.objects.order_by('nombre')
    return { 'states': states,
             'providers': providers }
