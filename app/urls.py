from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
#    url(r'^$', views.login, name='login'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    # url('^login/',
    #   'django.contrib.auth.views.login',
    #   {'template_name': 'login.html'}
    # ),
    url(r'^$', views.index, name='index'),
)
