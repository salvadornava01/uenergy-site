from django.contrib import admin

# Register your models here.
from .models import Contactos

class ContactosAdmin(admin.ModelAdmin):
    search_fields=('nombreComp','empresa','telefono')
    list_display = ('nombreComp', 'telefono', 'empresa', 'timestamp')
    readonly_fields = ("timestamp",)
    class Meta:
        model = Contactos
admin.site.register(Contactos, ContactosAdmin)