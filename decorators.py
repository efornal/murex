# -*- coding: utf-8 -*-
from django.shortcuts import redirect
import logging
from django.contrib import messages
from django.utils.translation import ugettext as _


def toner_permission_required(view):
    def wrap(request, *args, **kwargs):
        permissions = ['app.change_toner']
        if not request.user.has_perms(permissions):
            logging.error("The user '{}' does not have permissions on {}" \
                          .format(request.user,permissions))
            messages.warning(request, _('user_without_permissions'))
            return redirect('logout')
        else:
            return view(request, *args, **kwargs)
        
    return wrap
