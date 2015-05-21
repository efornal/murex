from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('app.views',
    url(r'^logout/$', 'logout_view', name='logout'),
    url('^login/','login_view', name='login'),
    url('^toners/por_modelos/','toners_por_modelos', name='toners_por_modelos'),
    url('^toners/','toners', name='toners'),
    url(r'^toner/(\d+)/$', 'toner', name='toner'),
    url('^search/','search', name='search'),
    url(r'^toner/(\d+)/detail/$', 'toner_detail', name='toner_detail'),
    url(r'^$', 'index', name='index'),
)
