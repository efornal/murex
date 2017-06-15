# -*- coding: utf-8 -*-
from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^login/',views.login_view, name='login'),
    url(r'^toners/por_modelos/',views.toners_por_modelos, name='toners_por_modelos'),
    url(r'^toners/por_estados/',views.toners_por_estados, name='toners_por_estados'),
    url(r'^toners/filtrar/',views.filtrar_listado, name='filtrar_listado'),
    url(r'^toners/',views.toners, name='toners'),
    url(r'^toner/(\d+)/$', views.toner, name='toner'),
    url(r'^search/',views.search, name='search'),
    url(r'^toner/(\d+)/detail/$', views.toner_detail, name='toner_detail'),
    url(r'^lang/(?P<lang>\w+)/$', views.set_language, name='set_language'),
    url(r'^$', views.index, name='index'),
]

