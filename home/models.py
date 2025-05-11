# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Clientes(models.Model):

    #__Clientes_FIELDS__
    idclientes = models.IntegerField(null=True, blank=True)
    nombrecliente = models.TextField(max_length=255, null=True, blank=True)
    direccion = models.TextField(max_length=255, null=True, blank=True)
    telefono = models.TextField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)

    #__Clientes_FIELDS__END

    class Meta:
        verbose_name        = _("Clientes")
        verbose_name_plural = _("Clientes")


class Tiposervicio(models.Model):

    #__Tiposervicio_FIELDS__
    idtiposervicio = models.IntegerField(null=True, blank=True)
    nombreservicio = models.TextField(max_length=255, null=True, blank=True)
    precio = models.IntegerField(null=True, blank=True)

    #__Tiposervicio_FIELDS__END

    class Meta:
        verbose_name        = _("Tiposervicio")
        verbose_name_plural = _("Tiposervicio")


class Servicos(models.Model):

    #__Servicos_FIELDS__
    idclientes = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    idtiposervicio = models.ForeignKey(TipoServicio, on_delete=models.CASCADE)
    fechaintal = models.DateTimeField(blank=True, null=True, default=timezone.now)
    fechacobro = models.DateTimeField(blank=True, null=True, default=timezone.now)
    direccion = models.TextField(max_length=255, null=True, blank=True)
    gps = models.TextField(max_length=255, null=True, blank=True)
    activo = models.BooleanField()
    idzona = models.ForeignKey(Zonas, on_delete=models.CASCADE)
    idcobrador = models.IntegerField(null=True, blank=True)
    nota = models.TextField(max_length=255, null=True, blank=True)
    idservicio = models.IntegerField(null=True, blank=True)

    #__Servicos_FIELDS__END

    class Meta:
        verbose_name        = _("Servicos")
        verbose_name_plural = _("Servicos")


class Zonas(models.Model):

    #__Zonas_FIELDS__
    idzona = models.IntegerField(null=True, blank=True)
    nombrezona = models.TextField(max_length=255, null=True, blank=True)

    #__Zonas_FIELDS__END

    class Meta:
        verbose_name        = _("Zonas")
        verbose_name_plural = _("Zonas")


class Cobradores(models.Model):

    #__Cobradores_FIELDS__
    idcobrador = models.IntegerField(null=True, blank=True)
    nombrecobrador = models.TextField(max_length=255, null=True, blank=True)
    activo = models.BooleanField()

    #__Cobradores_FIELDS__END

    class Meta:
        verbose_name        = _("Cobradores")
        verbose_name_plural = _("Cobradores")


class Resivos(models.Model):

    #__Resivos_FIELDS__
    idresivo = models.IntegerField(null=True, blank=True)
    idservicio = models.ForeignKey(Servicos, on_delete=models.CASCADE)
    fechageneracion = models.DateTimeField(blank=True, null=True, default=timezone.now)
    monto = models.IntegerField(null=True, blank=True)

    #__Resivos_FIELDS__END

    class Meta:
        verbose_name        = _("Resivos")
        verbose_name_plural = _("Resivos")



#__MODELS__END
