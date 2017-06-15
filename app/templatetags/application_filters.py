from django import template
from django.template.defaultfilters import stringfilter
from django.conf import settings
import logging

register = template.Library()

@register.filter
def application_title(value):
    title = ''
    if value:
        title = value
    elif settings.APPLICATION_NAME:
        title = settings.APPLICATION_NAME

    return title

@register.filter
def application_subtitle(value):
    subtitle = ''
    if value:
        subtitle = value
    elif settings.APPLICATION_DESC:
        subtitle = settings.APPLICATION_DESC

    return subtitle


def class_listings(arg):
    return ['info', 'warning']


@register.filter(name='class_listings')
@stringfilter
def class_listing(arg,position):
    return ['info', 'warning'][position]


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
        return 'remove.png' # Dado de baja
    elif state == 5:
        return 'share-alt.png' # En devolucion
    elif state == 4:
        return 'retweet.png' # En stock vacio
    elif state == 3:
        return 'lock.png' # En stock cargado
    elif state == 2:
        return 'wrench.png' # En Proveedor
    elif state == 1:
        return 'print.png' # En impresora

    
@register.filter(name='icon_by_status_tag')
@stringfilter
def icon_by_status_tag(arg, state):
    icon = icon_by_status(None,state)
    return ("<img src='%s%s/%s' \>"  % ( settings.STATIC_URL, 'images', icon) )

