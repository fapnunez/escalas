from django.contrib import admin
from .models import (
    Medico,
    Posto, 
    Folga, 
    Escala
)

class Cad_manual_escalasAdmin(admin.ModelAdmin):
    list_display = ('data', 'posto', 'medico')

admin.site.register(Medico)
admin.site.register(Posto)
admin.site.register(Folga)
admin.site.register(Escala, Cad_manual_escalasAdmin)

# Register your models here.
