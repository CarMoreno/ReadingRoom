from django import forms
from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
from biblioteca.models import Libro, Autor, Editor
from django.http import HttpResponseRedirect
from django.shortcuts import render


class FormContacto(forms.Form):
    # TODO: Define form fields here
    asunto = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='E-mail (opcional)')#El campo email no es requerido
    mensaje = forms.CharField(widget=forms.Textarea)    
    
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
    	                   
