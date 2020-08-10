
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
# Create your models here.

class Remitente(models.Model):
    Nombre = models.CharField(max_length=45)
    Apellido = models.CharField(max_length=45)
    Telefono = models.CharField(max_length=45)
    DNI = models.CharField(max_length=45)
    def __str__(self):
        return self.Nombre

class Destinatario(models.Model):
    Nombre = models.CharField(max_length=45)
    Apellido = models.CharField(max_length=45)
    Telefono = models.CharField(max_length=45)
    DNI = models.CharField(max_length=45)
    def __str__(self):
        return self.Nombre

class Movilidad(models.Model):
    Conductor= models.CharField(max_length=45)
    Marca = models.CharField(max_length=45)
    Placa = models.CharField(max_length=45)
    Certificado = models.CharField(max_length=45)
    Licencia = models.CharField(max_length=45)
    def __str__(self):
        return self.Conductor

class Encomienda(models.Model):
    Tipo = models.CharField(max_length=45)
    Peso = models.CharField(max_length=45)
    Descripcion = models.CharField(max_length=45)
    Pago = models.CharField(max_length=45)
    Estado = models.CharField(max_length=45)

    def __str__(self):
        return self.Tipo

class GuiaRemision(models.Model):
    Remitente = models.ForeignKey(Remitente, default=1, on_delete=models.SET_DEFAULT)
    Destinatario=models.ForeignKey(Destinatario, default=1, on_delete=models.SET_DEFAULT)
    Movilidad = models.ForeignKey(Movilidad, default=1, on_delete=models.SET_DEFAULT)
    Encomienda=models.ForeignKey(Encomienda, default=1, on_delete=models.SET_DEFAULT)
    Sucursal=models.CharField(max_length=45)
    Partida = models.CharField(max_length=45)
    Llegada = models.CharField(max_length=45)
    Fecha = models.DateField()

    def __str__(self):
        return self.Sucursal