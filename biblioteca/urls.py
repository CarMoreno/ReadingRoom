from django.conf.urls import url 
from . import views #Dee ste directorio importe views

urlpatterns = [
	url(r'^$', views.LibroListView.as_view(), name='index'),
	url(r'^contactos/$', views.contactos, name='contactos'),
	url(r'^buscar/$', views.buscar, name='buscar'),
	url(r'^contactos/gracias$', views.gracias, name='gracias'),
	url(r'^crearlibro$', views.crear, name='crear')
]