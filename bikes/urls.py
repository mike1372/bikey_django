from django.conf.urls import url

from . import views

urlpatterns = [
		url(r'^$', views.index, name='index'),
		url(r'^about/$', views.about, name='about'),
		url(r'^new/$', views.new, name='new'),
		url(r'^add/$', views.add, name='add'),
		url(r'^(?P<bike_id>[0-9]+)/$', views.show, name='show'),
		url(r'^(?P<bike_id>[0-9]+)/edit/$', views.edit, name='edit'),
		url(r'^(?P<bike_id>[0-9]+)/update/$', views.update, name='update'),
		url(r'^(?P<bike_id>[0-9]+)/delete/$', views.delete, name='delete'),
		url(r'^(?P<bike_id>[0-9]+)/add_chainring/$', views.add_chainring, name='add_chainring'),
		url(r'^(?P<bike_id>[0-9]+)/add_cassettesprocket/$', views.add_cassettesprocket, name='add_cassettesprocket'),
		]