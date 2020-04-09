from django.test import TestCase, Client
from django.urls import reverse
from homepage.models import Contactos

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home_view')
        self.clientes_url = reverse('clientes_view')
        self.instalaciones_url = reverse('instalaciones_view')
        self.plantas_url = reverse('plantas_view')
        self.aire_url = reverse('aire_view')
        self.upss_url = reverse('upss_view')
        self.reguladores_url = reverse('reguladores_view')
        self.contact_form_url = reverse('contact_form_view')

    def test_home_view_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
    
    def test_clientes_view_GET(self):
        response = self.client.get(self.clientes_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'clientes.html')
    
    def test_instalaciones_view_GET(self):
        response = self.client.get(self.instalaciones_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'instalaciones.html')
    
    def test_plantas_view_GET(self):
        response = self.client.get(self.plantas_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'plantas.html')
    
    def test_aire_view_GET(self):
        response = self.client.get(self.aire_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'airea.html')
    
    def test_upss_view_GET(self):
        response = self.client.get(self.upss_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'upss.html')
    
    def test_reguladores_view_GET(self):
        response = self.client.get(self.reguladores_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'reguladores.html')

    def test_contact_form_view_POST(self):
        
        response = self.client.post(self.contact_form_url, {
            'nombre_y_apellidos':'Test Case',
            'numero_tel':'0123456789',
            'email':'test@test.com',
            'mensaje':'Message Test From Test',
        })

        self.assertEquals(response.status_code, 200)