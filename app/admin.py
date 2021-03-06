from django.contrib import admin
from app.models import Proveedor, Oficina, Impresora, Estado, Toner

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono')
    search_fields = ['nombre','direccion','telefono']

    
class TonerAdmin(admin.ModelAdmin):
    list_display = ('identificador', 'marca', 'modelo')
    list_filter = ('marca','modelo')

admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Oficina)
admin.site.register(Impresora)
admin.site.register(Toner, TonerAdmin)

