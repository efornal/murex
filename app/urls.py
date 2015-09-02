from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('app.views',
    url(r'^logout/$', 'logout_view', name='logout'),
    url(r'^login/','login_view', name='login'),
    url(r'^toners/por_modelos/','toners_por_modelos', name='toners_por_modelos'),
    url(r'^toners/por_estados/','toners_por_estados', name='toners_por_estados'),
    url(r'^toners/filtrar/','filtrar_listado', name='filtrar_listado'),
    url(r'^toners/','toners', name='toners'),
    url(r'^toner/(\d+)/$', 'toner', name='toner'),
    url(r'^search/','search', name='search'),
    url(r'^toner/(\d+)/detail/$', 'toner_detail', name='toner_detail'),
    url(r'^$', 'index', name='index'),
)

