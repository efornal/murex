from django import template
from django.template.defaultfilters import stringfilter
import logging

register = template.Library()


@register.filter(name='class_intersection')
@stringfilter
def class_intersection(arg,enable):
    if enable:
        return 'intersection'
    return ''


@register.filter(name='icon_by_status')
@stringfilter
def icon_by_status(arg, state):
    if state == 6:
        return 'glyphicon-remove' # Dado de baja
    elif state == 5:
        return 'glyphicon-share-alt' # En devolucion
    elif state == 4:
        return ' glyphicon-retweet' # En stock vacio
    elif state == 3:
        return 'glyphicon-lock' # En stock cargado
    elif state == 2:
        return 'glyphicon-wrench' # En Proveedor
    elif state == 1:
        return 'glyphicon-print' # En impresora

    
@register.filter(name='icon_by_status_tag')
@stringfilter
def icon_by_status_tag(arg, state):
    icon_class = icon_by_status(None,state)
    return ("<i class='glyphicon %s'></i>"  % icon_class)
