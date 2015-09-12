from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from biblioteca.models import Libro, Editor, Autor#Importamos modelos
from biblioteca.forms import FormContacto, FormCrearLibro#Importamos los formularios creados con la api de forms
from django.views.generic import ListView, DetailView #Listas genericas de Django
from django.views.generic.edit import CreateView, UpdateView, DeleteView#Listas genericas de Django
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
TAMANO_QUERY_BUSQUEDA = 100 

class LibroListView(ListView):
	"""Clase-Vista generica que mostrara en una lista todos los Libros guardados en la BD,
	debemos de hacer un template con el nombre que django buscara por default, en este caso
	es libro_list.html, sino definimos el nombre con el atributo template_name"""
	model = Libro
	template_name = 'biblioteca/index.html'
	context_object_name = "lista_libros" #El contexto que usaremos en la template

class LibroCreateView(CreateView):
	model = Libro
	form_class = FormCrearLibro #Caracteristicas especiales para este formulario
	template_name = 'biblioteca/uc_libro.html'

	def get_context_data(self, **kwargs):
		"""Para poder mandar contextos extras a las vistas"""
		# Call the base implementation first to get a context
		context = super(CreateView, self).get_context_data(**kwargs)
		context["now_create"] = True
		return context

class LibroUpdateView(UpdateView):
	"""Clase-Vista generica que mostrara los datos de un libro para que este sea editado"""
	model = Libro
	form_class = FormCrearLibro
	template_name = 'biblioteca/uc_libro.html'

class LibroDetailView(DetailView):
	"""Clase-Vista generica que mostrara los detalles de un libro para que podamos conocerlo mejor :)"""
	model = Libro
	template_name = 'biblioteca/detalles_libro.html'	

class LibroDeleteView(DeleteView):
	model = Libro
	success_url = reverse_lazy('sitio:index')#Hacia donde me redirige despues de eliminar un libro
#_____________________________________________________________________________________________________
def buscar(request):
	"""Busca por nombre, libros en la base de datos"""
	errors = []

	if 'query' in request.GET:
		query = request.GET['query']#hasta aca puede que query sea una cadena vacia (que para python es como si fuere un False)
		if not query:
			errors.append('Por favor digita un criterio de busqueda') #si entra aca es porque el query estaba vacio
		elif len(query)>TAMANO_QUERY_BUSQUEDA:
			errors.append('Por favor digita un criterio de busqueda menor a 100 caracteres')
		else:
			libros = Libro.objects.filter(titulo__icontains=query)#Icontains es un tipo de busqueda que no tiene en cuenta mayusculas o minusculas
			return render(request, 'biblioteca/resultados.html', {'query':query, 'libros':libros})#Con los objetos obtenidos simplemente los mando a la template
	
	return render(request, 'biblioteca/buscar.html', {'errors':errors})#Hubo un error??
#____________________________________________________________________________________________________

	
#_________________________________________________________________________________________________
def contactos(request):
	"""Crear y valida un formulario de contactos usando la api de formularios"""
	errors = []
	if request.method == 'POST':
		form = FormContacto(request.POST)
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
		form = FormContacto()
	return render(request,'biblioteca/contactos.html', {'form':form})
		
#__________________________________________________________________________________________________
def gracias(request):
	"""Retorna una pagina de gracias despues de que el formulario de contactos ha sido enviado con exito"""
	return render(request, 'biblioteca/gracias.html')
#____________________________________________________________________________________________________
    
