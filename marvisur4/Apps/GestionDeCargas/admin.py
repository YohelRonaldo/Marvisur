from django.contrib import admin

from .models import *
# Register your models here.

class Remitentes(admin.ModelAdmin):
    list_display=("Nombre","Apellido","Telefono","DNI")

class Destinatarios(admin.ModelAdmin):
    list_display=("Nombre","Apellido","Telefono","DNI")

class Movilidades(admin.ModelAdmin):
    list_display=("Conductor","Marca","Placa","Certificado","Licencia")

class Encomiendas(admin.ModelAdmin):
    list_display=("Tipo","Peso","Descripcion","Pago","Estado")

class GuiasRemision(admin.ModelAdmin):
    list_display=("Sucursal","Partida","Llegada","Fecha")

admin.site.register(Remitente,Remitentes)
admin.site.register(Destinatario,Destinatarios)
admin.site.register(Movilidad,Movilidades)
admin.site.register(Encomienda,Encomiendas)

admin.site.register(GuiaRemision,GuiasRemision)