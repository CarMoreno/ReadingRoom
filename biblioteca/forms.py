from django import forms
from django.forms import ModelForm
from biblioteca.models import Libro, Autor, Editor

class FormContacto(forms.Form):
    # TODO: Define form fields here
    asunto = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='E-mail (opcional)')#El campo email no es requerido
    mensaje = forms.CharField(widget=forms.Textarea)

# class FormCrearLibro(forms.Form):
# 	titulo = forms.CharField(max_length=100)
# 	autor = forms.ModelMultipleChoiceField(label='Autor(es)', queryset= Autor.objects.all())#M2M
# 	editor = forms.ModelChoiceField(queryset = Editor.objects.all())#PK
# 	fecha_publicacion = forms.DateField(required=False, label='Fecha de Publiciacion(Opcional)')
# 	portada = forms.ImageField(required=False)    
    
class FormCrearAutor(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'email']

class FormCrearEditor(forms.ModelForm):
        class Meta:
            model = Editor
            fields = ['nombre','domicilio', 'ciudad', 'estado', 'pais', 'website']
            
class FormCrearLibro(forms.ModelForm):
    class Meta:
        model = Libro
    	fields = ['titulo', 'autores', 'editor', 'fecha_publicacion', 'portada', 'sinopsis']
    	
