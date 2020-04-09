from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import datetime
import os


def smtp_api_mail(html_mssg,subj,emailto,emailfrom):
    
    plain_message = strip_tags(html_mssg)
            #################################### Envio a CLIENTE ###################################
    dominios_redireccionados = ['@hotmail', '@outlook', '@live']
    direccion_checar = emailto
        send_mail(subj, plain_message, 'bhip_lsm@hotmail.com', [emailto,],fail_silently=False, html_message=html_mssg)
    else:
        message = Mail(
                        from_email = From(emailfrom), #'"Bhip MX LSM" <asesoria@bhip.mx>'
                        to_emails = To(emailto),
                        subject=subj,
                        html_content=html_mssg)
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
        except Exception as e:
                print('Error!')
                print(e)
    return 'mail sent to: ' + emailto