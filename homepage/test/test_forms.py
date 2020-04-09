from django.test import SimpleTestCase
from homepage.forms import ContactForm, CotizForm


class TestForms(SimpleTestCase):

    def test_client_form_valid(self):
        form = ContactForm(data={
            'nombre_y_apellidos':'Test Case',
            'numero_tel':'0123456789',
            'email':'test@test.com',
            'mensaje':'Message Test From Test',
        })

        self.assertTrue(form.is_valid())

    def test_client_form_valid(self):
        form = CotizForm(data={
            'nombre_completo':'Test Case',
            'empresa':'Test Test',
            'numero_telefonico':'0123456789',
            'email_de_contacto':'test@test.com',
            'mensaje_de_solicitud':'Message Test From Test',
        })

        self.assertTrue(form.is_valid())