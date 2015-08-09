from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from biblioteca.models import Libro, Editor, Autor#Importamos modelos
from biblioteca.forms import FormularioContacto, FormularioCrear#Importamos los formularios creados con la api de forms
from django.views.generic import ListView, DetailView #Listas genericas de Django
# Create your views here.
TAMANO_QUERY_BUSQUEDA = 100 
class LibroListView(ListView):
	"""Clase generica que mostrara en una lista todos los Libros guardados en la BD,
	debemos de hacer un template con el nombre que django buscara por default, en este caso
	es libro_list.html, sino definimos el nombre con el atributo template_name"""
	model = Libro
	template_name = 'biblioteca/index.html'

# def index(request):
# 	"""En el index se mostrara la lista de libros que tenemos en la base de datos"""
# 	return render(request, "biblioteca/index.html")
#_____________________________________________________________________________________________________
def buscar(request):
	"""Busca por nombre, libros en la base de datos"""
	errors = []

	if 'query' in request.GET:
		query = request.GET['query']#hasta aca puede que query sea una cadena vacia (que para python es como si fuere un False)
		if not query:
			errors.append('Por favor digita un criterio de busqueda') #si entra aca es porque el query estaba vacio
		elif len(query)>TAMANO_QUERY_BUSQUEDA:
			errors.append('Por favor digita un criterio de busqueda menor a 20 caracteres')
		else:
			libros = Libro.objects.filter(titulo__icontains=query)#Icontains es un tipo de busqueda que no tiene en cuenta mayusculas o minusculas
			return render(request, 'biblioteca/resultados.html', {'query':query, 'libros':libros})#Con los objetos obtenidos simplemente los mando a la template
	
	return render(request, 'biblioteca/buscar.html', {'errors':errors})#Hubo un error??
#____________________________________________________________________________________________________

def crear(request):
	return render(request, 'biblioteca/crear.html', {'respuesta':'En proceso'})
	# errors = []
	# autor = Autor()
	# editor = Editor()
	# if request.method == 'POST':
	# 	form = FormularioCrear(request.POST)
	# 	if form.is_valid():
	# 		cd = form.cleaned_data
	# 		# Autor.nombre = cd['autor']#Nombre del autor
	# 		# Editor.nombre = cd['editor']#Nombre del editor
	# 		Libro.objects.create(titulo=cd['titulo'], autores = Autor(), editor = Editor(), fecha_publicacion = cd['fecha_publicacion'], portada=cd['portada'])
	# 		return render(request, 'biblioteca/crear.html', {'respuesta':'OK'})

	# else:
	# 	form = FormularioCrear()		
	# return render(request, 'biblioteca/crear.html', {'form':form})		

	
#_________________________________________________________________________________________________
def contactos(request):
	"""Crear y valida un formulario de contactos usando la api de formularios"""
	errors = []
	if request.method == 'POST':
		form = FormularioContacto(request.POST)
		if form.is_valid():
			cd = form.cleaned_data #Esta linea es muy importante: {'mensaje': u'Buen sitio!', 'email': u'adrian@example.com', 'asunto': u'Hola'}, me pasa de codig html a codigo python todos los campos del formulario
			# send_email(
			# 	cd['asunto'],
			# 	cd['mensaje'],
			# 	cd.get('email', 'norelpyexample.com'),
			# 	['siteowner@example.com'],	
			# )
			# return HttpResponseRedirect(reverse('sitio:con'))
			return render(request, 'biblioteca/gracias.html', {'asunto':cd['asunto'], 'mensaje':cd['mensaje'], 'email':cd['email'], 'open_modal':True})
	else:
		form = FormularioContacto()
	return render(request,'biblioteca/contactos.html', {'form':form})

		
#__________________________________________________________________________________________________
def gracias(request):
	"""Retorna una pagina de gracias despues de que el formulario de contactos ha sido enviado con exito"""
	return render(request, 'biblioteca/gracias.html')			