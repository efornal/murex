from django import template
from django.template.defaultfilters import stringfilter
import logging

register = template.Library()



# dado de baja: glyphicon-remove
# En devolucion: glyphicon-share-alt
# En stock vacio: glyphicon-retweet
# En stock cargado: glyphicon-lock
# En Proveedor: glyphicon-tent
# en impresora: glyphicon-print
@register.filter(name='icon_by_status')
@stringfilter
def icon_by_status(arg, state):
    logging.error("ERR %s" % state)
    if state == 6:
        return 'glyphicon-remove'
    elif state == 5:
        return 'glyphicon-share-alt'
    elif state == 4:
        return ' glyphicon-retweet'
    elif state == 3:
        return 'glyphicon-lock'
    elif state == 2:
        return 'glyphicon-wrench'
    elif state == 1:
        return 'glyphicon-print'
 
