from django.conf.urls import url 
from . import views #Dee ste directorio importe views

urlpatterns = [
	#Index
	url(r'^$', views.LibroListView.as_view(), name='index'),
	#Formulario de contactos
	url(r'^contactos/$', views.contactos, name='contactos'),
	#Buscador
	url(r'^buscar/$', views.buscar, name='buscar'),
	#Agradecimiento
	url(r'^contactos/gracias$', views.gracias, name='gracias'),
	#Subir libros
	url(r'^crearlibro$', views.LibroCreateView.as_view(), name='crear'),
	#Update Libros
	url(r'^(?P<pk>\d+)/updatelibro$', views.LibroUpdateView.as_view(), name='update'),
]