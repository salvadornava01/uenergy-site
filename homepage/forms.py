from django import forms

from django.core.validators import RegexValidator

class ContactForm(forms.Form):
    letters_only = RegexValidator(r'^[ÁÉÍÓÚáéíóúñÑüÜÀÈÌÒÙàèìòù.A-Za-z ]*$', 'Sólo se permiten letras en este campo.')
    digits_only = RegexValidator(r'^[0-9]*$', 'Sólo se permiten dígitos en este campo.')
    nombre_y_apellidos = forms.CharField(max_length=50, validators=[letters_only], 
    widget= forms.TextInput(
        attrs={
                'class': 'form-control',
                'title': 'Nombre completo',
                'pattern':'[ÁÉÍÓÚáéíóúñÑüÜÀÈÌÒÙàèìòù.A-Za-z ]+',
                'oninvalid':"this.setCustomValidity('Escriba su nombre. Sólo se permiten letras en este campo.')",
                'oninput':"this.setCustomValidity('')"
        }
    ))
    numero_tel = forms.CharField(widget=forms.TextInput(
            attrs={
                    'class': 'form-control',
                    'pattern':'[0-9]+', 'title':'Sólo se permiten dígitos en este campo.',
                    'oninvalid':"this.setCustomValidity('Escriba su número de teléfono a diez dígitos. Sólo números permitidos en este campo.')",
                    'oninput':"this.setCustomValidity('')"
            }
    ),max_length=10,min_length=10,validators=[digits_only])
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control'
        }

    ))
    mensaje = forms.CharField(max_length=500, widget=forms.Textarea(
        attrs={
            'class': 'form-control'
        }
    ))

class CotizForm(forms.Form):
    letters_only = RegexValidator(r'^[ÁÉÍÓÚáéíóúñÑüÜÀÈÌÒÙàèìòù.A-Za-z ]*$', 'Sólo se permiten letras en este campo.')
    digits_only = RegexValidator(r'^[0-9]*$', 'Sólo se permiten dígitos en este campo.')
    nombre_completo = forms.CharField(max_length=50, validators=[letters_only], 
    widget= forms.TextInput(
        attrs={
                'class': 'form-control',
                'title': 'Nombre completo',
                'pattern':'[ÁÉÍÓÚáéíóúñÑüÜÀÈÌÒÙàèìòù.A-Za-z ]+',
                'oninvalid':"this.setCustomValidity('Escriba su nombre. Sólo se permiten letras en este campo.')",
                'oninput':"this.setCustomValidity('')"
        }
    ))
    empresa = forms.CharField(max_length=50, validators=[letters_only], 
    widget= forms.TextInput(
        attrs={
                'class': 'form-control',
                'title': 'Nombre completo',
                'pattern':'[ÁÉÍÓÚáéíóúñÑüÜÀÈÌÒÙàèìòù.A-Za-z ]+',
                'oninvalid':"this.setCustomValidity('Escriba el nombre de su empresa u organización.  Sólo se permiten letras en este campo.')",
                'oninput':"this.setCustomValidity('')"
        }
    ))
    numero_telefonico = forms.CharField(widget=forms.TextInput(
            attrs={
                    'class': 'form-control',
                    'pattern':'[0-9]+', 'title':'Sólo se permiten dígitos en este campo.',
                    'oninvalid':"this.setCustomValidity('Escriba su número de teléfono a diez dígitos. Sólo números permitidos en este campo.')",
                    'oninput':"this.setCustomValidity('')"
            }
    ),max_length=10,min_length=10,validators=[digits_only])
    email_de_contacto = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control'
        }

    ))
    mensaje_de_solicitud = forms.CharField(max_length=500, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Describa su necesidad'
        }
    ))