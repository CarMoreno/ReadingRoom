from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Editor(models.Model):
	nombre = models.CharField(max_length=30)
	domicilio = models.CharField(max_length=50)
	ciudad = models.CharField(max_length=60)
	estado = models.CharField(max_length=30)
	pais = models.CharField(max_length=50)
	website = models.URLField()

	def __unicode__(self):#__str__ para python 3
		return self.nombre

	def get_absolute_url(self):
		return reverse('sitio:index')

	class Meta:
		verbose_name_plural = 'Editores'

#____________________________________________________________			
class Autor(models.Model):
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=40)
	email = models.EmailField(blank=True, verbose_name='e-mail')#CAMPO EMAIL OPCIONAL, con el verbose_name persoalizamos el label que se muestra para el campo en el form

	def __unicode__(self):#__str__ para python 3
		cadena = "%s %s" %(self.nombre, self.apellido)
		return cadena

	def get_absolute_url(self):
		return reverse('sitio:index')

	class Meta:
		ordering = ["nombre"]#Por default, Siempre ordenara por nombre todos los registros
		verbose_name_plural='Autores'	


class Libro(models.Model):
	titulo = models.CharField(max_length=100)
	autores = models.ManyToManyField(Autor, default=Autor.objects.filter(pk=1)) # Un libro, puede ser escrito por muchos autores, y un autor puede escribir muchos libros (Relacion muchos a muchos entre libro y autor)
	editor = models.ForeignKey(Editor, default=Editor.objects.filter(pk=1))	#Un editor puede distribuir muchos libros, pero un libro solo puede ser distribuido por un solo editor (Relacion uno a muchos entre libros y editor, tambien conocida como llave foranea)
	fecha_publicacion = models.DateField(help_text='Usa el formato DD/MMM/YYYY')
	portada = models.ImageField(upload_to = 'portadas/', null=True, blank=True)#Crea una carpeta donde guarara las imagenes de las portadas, al final la imagen tendra que cargarse en: media/portadas/
	sinopsis = models.TextField(blank=True)

	def get_absolute_url(self):
		return reverse('sitio:index')
	
	def __unicode__(self):#__str__ para python 3
		return self.titulo
