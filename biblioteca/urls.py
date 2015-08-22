from django.conf.urls import url 
from . import views #De este directorio importe views

urlpatterns = [
	#Index
	url(r'^catalogo$', views.LibroListView.as_view(), name='catalogo'),
	#Formulario de contactos
	url(r'^contactos/$', views.contactos, name='contactos'),
	#Buscador
	url(r'^buscar/$', views.buscar, name='buscar'),
	#Agradecimiento
	url(r'^contactos/gracias$', views.gracias, name='gracias'),
	#Subir libros
	url(r'^crear-libro$', views.LibroCreateView.as_view(), name='crear'),
	#Update Libros
	url(r'^(?P<pk>\d+)/update-libro$', views.LibroUpdateView.as_view(), name='update'),
	#Detail Libros
	url(r'^(?P<pk>\d+)/detalles-libro$', views.LibroDetailView.as_view(), name='detail'),
	# #Registrarse
	# url(r'^$', views.registrarse, name="registrarse"),
]