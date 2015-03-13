from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('app.views',
    url(r'^logout/$', 'logout_view', name='logout'),
    url('^login/','login_view', name='login'),
    url('^toners/','toners', name='toners'),
    url('^search/','search', name='search'),
    url(r'^$', 'index', name='index'),
)
