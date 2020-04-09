from django.db import models
from django.utils.encoding import smart_text
import  uuid

# Create your models here.

class Contactos(models.Model):

    nombreComp = models.CharField(max_length=120, null=True, blank=False)
    empresa = models.CharField(max_length=120, null=True, blank=True)
    telefono = models.CharField(max_length=10, null=True, blank=False)
    email = models.EmailField()
    mensaje = models.TextField(blank=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, )
    updated = models.DateTimeField(auto_now_add=False, auto_now=True) 
    
    def __str__(self):
        return smart_text(self.nombreComp)