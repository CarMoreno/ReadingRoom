from django import forms

class FormularioContacto(forms.Form):
    # TODO: Define form fields here
    asunto = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='E-mail (opcional)')#El campo email no es requerido
    mensaje = forms.CharField(widget=forms.Textarea)

class FormularioCrear(forms.Form):
	titulo = forms.CharField(max_length=100)
	autor = forms.CharField(label='Autor(es)')
	editor = forms.CharField(max_length=50)
	fecha_publicacion = forms.DateField(required=False, label='Fecha de Publiciacion(Opcional)')
	portada = forms.ImageField(required=False)    
    
