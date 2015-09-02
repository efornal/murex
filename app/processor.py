from app.models import Estado, Proveedor

def states(request):
    return {'states': Estado.objects.order_by('nombre')}

def providers(request):
    return {'providers': Proveedor.objects.order_by('nombre')}

