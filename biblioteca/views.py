from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from biblioteca.models import Libro, Editor, Autor
from biblioteca.forms import FormularioContacto, FormularioCrear
# Create your views here.
def index(request):
	return render(request, "biblioteca/index.html")
#_____________________________________________________________________________________________________
def buscar(request):
	errors = []

	if 'query' in request.GET:
		query = request.GET['query']#hasta aca puede que query sea una cadena vacia (que para python es como si fuere un False)
		if not query:
			errors.append('Por favor digita un criterio de busqueda') #si entra aca es porque el query estaba vacio
		elif len(query)>20:
			errors.append('Por favor digita un criterio de busqueda menor a 20 caracteres')
		else:
			libros = Libro.objects.filter(titulo__icontains=query)#Icontains es un tipo de busqueda que no tiene en cuenta mayusculas o minusculas
			libroas_obj = Libro.objects.get(titulo__icontains=query)#Obtengo el registro del libro como un objeto, arriba lo obtengo es como un arreglo de objetos
			autores = libroas_obj.autores.all()#Obtengo los autores del libro asociado. Autor es un objeto tambien, por lo que puedo acceder a metodos como get(), all(), etc.
			return render(request, 'biblioteca/resultados.html', {'query':query, 'libros':libros, 'autores':autores})#Con los objetos obtenidos simplemente los mando a la template
	
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
			return HttpResponseRedirect(reverse('sitio:gracias'))
			# return render(request, 'biblioteca/gracias.html', {'asunto':cd['asunto']})
	else:
		form = FormularioContacto()
	return render(request,'biblioteca/contactos.html', {'form':form})

		
#__________________________________________________________________________________________________
def gracias(request):
	return render(request, 'biblioteca/gracias.html')			