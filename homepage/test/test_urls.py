from django.test import SimpleTestCase
from django.urls import reverse, resolve
from homepage.views import *

class TestUrls(SimpleTestCase):

    def test_homepage_resolved(self):
        url = reverse('home_view')
        self.assertEquals(resolve(url).func, home_view)
    def test_clientes_resolved(self):
        url = reverse('clientes_view')
        self.assertEquals(resolve(url).func, clientes_view)
    def test_instalaciones_resolved(self):
        url = reverse('instalaciones_view')
        self.assertEquals(resolve(url).func, instalaciones_view)
    def test_plantas_resolved(self):
        url = reverse('plantas_view')
        self.assertEquals(resolve(url).func, plantas_view)
    def test_aire_resolved(self):
        url = reverse('aire_view')
        self.assertEquals(resolve(url).func, aire_view)
    def test_upss_resolved(self):
        url = reverse('upss_view')
        self.assertEquals(resolve(url).func, upss_view)
    def test_reguladores_resolved(self):
        url = reverse('reguladores_view')
        self.assertEquals(resolve(url).func, reguladores_view)
    def test_contact_form_resolved(self):
        url = reverse('contact_form_view')
        self.assertEquals(resolve(url).func, contact_form_view)
    def test_cotiz_form_resolved(self):
        url = reverse('cotiz_form_view')
        self.assertEquals(resolve(url).func, cotiz_form_view)
    def test_thankyoupage_resolved(self):
        url = reverse('thankyoupage_view', args=['id'])
        self.assertEquals(resolve(url).func, thankyoupage_view)
