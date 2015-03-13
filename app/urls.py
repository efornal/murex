from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
#    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
#     url('^login/','django.contrib.auth.views.login',{'template_name': 'login.html'}),
    url('^login/',views.login, name='login'),
#    url('^logout/',views.logout, name='logout'),
    url('^toners/',views.toners, name='toners'),
    url(r'^$', views.index, name='index'),
)
