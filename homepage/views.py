import json

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from homepage.models import Contactos
from .forms import ContactForm, CotizForm
# Create your views here.

def home_view(request, *args, **kwargs):
    contactform = ContactForm()
    context = {'page_title':'Uenergy',
               'contactform':contactform}
    return render(request, 'home.html', context)

def clientes_view(request, *args, **kwargs):
    contactform = ContactForm()
    context = {'page_title':'Nuestros Clientes',
                'contactform':contactform}
    return render(request, 'clientes.html', context)

def instalaciones_view(request, *args, **kwargs):
    contactform = ContactForm()
    cotizform = CotizForm()
    context = {'page_title':'Instalaciones',
                'contactform':contactform,
                'cotizform':cotizform,
                }
    return render(request, 'instalaciones.html', context)

def plantas_view(request, *args, **kwargs):
    contactform = ContactForm()
    cotizform = CotizForm()
    context = {'page_title':'Plantas de Emergencia',
                'contactform':contactform,
                'cotizform':cotizform,
                }
    return render(request, 'plantas.html', context)

def aire_view(request, *args, **kwargs):
    contactform = ContactForm()
    cotizform = CotizForm()
    context = {'page_title':'Aire Acondicionado',
                'contactform':contactform,
                'cotizform':cotizform,
                }
    return render(request, 'airea.html', context)

def upss_view(request, *args, **kwargs):
    contactform = ContactForm()
    cotizform = CotizForm()
    context = {'page_title':"UPS's",
                'cotizform':cotizform,
                'contactform':contactform}
    return render(request, 'upss.html', context)

def reguladores_view(request, *args, **kwargs):
    contactform = ContactForm()
    cotizform = CotizForm()
    context = {'page_title':"Reguladores",
                'cotizform':cotizform,
                'contactform':contactform}
    return render(request, 'reguladores.html', context)

def contact_form_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # import pdb
            # pdb.set_trace()
            # print(form.cleaned_data)
            data = "Su mensaje ha sido enviado exitosamente. En breve un representante se pondrá en contacto con usted"
            datajson = json.dumps(data)
            return HttpResponse(datajson, content_type='application/json')
        else:
            print(form.errors)
            errors = form.errors
            datajson = json.dumps(errors)
            # import pdb
            # pdb.set_trace()
            return HttpResponseBadRequest(datajson, content_type='application/json')

def cotiz_form_view(request, *args, **kwargs):
    
    if request.method == 'POST':
        form = CotizForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            contacto_actual = Contactos(id=None,
                nombreComp = form_data['nombre_completo'],
                empresa = form_data['empresa'],
                telefono = form_data['numero_telefonico'],
                email = form_data['email_de_contacto'],
                mensaje = form_data['mensaje_de_solicitud'],
                )
            contacto_actual.save()
            # Send mail to admin
            nombre_contacto = form_data['nombre_completo']
            emailto = form_data['email_de_contacto']
            empresa_contacto = form_data['empresa']
            numero_contacto = form_data['numero_telefonico']
            mensaje_contacto = form_data['mensaje_de_solicitud']

            from_email = settings.EMAIL_HOST_USER
            html_mssg = render_to_string('emails/cotizacion_mail.html',{
                            'nombre_contacto':nombre_contacto,
                            'empresa_contacto':empresa_contacto,
                            'numero_contacto':numero_contacto,
                            'mensaje_contacto':mensaje_contacto,
                            })
            plain_message = strip_tags(html_mssg)
            # import pdb
            # pdb.set_trace()
            send_mail('Solicitud Cotizacion EPS Mexico', plain_message, from_email, [emailto, from_email],fail_silently=False, html_message=html_mssg)
            
            return HttpResponseRedirect(reverse('thankyoupage_view', kwargs={'id':contacto_actual.id}))

def thankyoupage_view(request, id, **kwargs):

    contactform = ContactForm()
    contacto_actual = Contactos.objects.get(id=id)
    nombre_contacto = contacto_actual.nombreComp
    context = {'nombre_contacto':nombre_contacto,
                'contactform':contactform,
                }
    return render(request, 'thankyou.html', context)
