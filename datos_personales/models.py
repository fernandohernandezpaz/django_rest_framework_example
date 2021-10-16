from django.db import models
from catalogos.models import Pais, Fotos
from django.contrib.auth.models import User


# Create your models here.
class Perfil(models.Model):
    nacionalidad = models.ForeignKey(Pais, on_delete=models.CASCADE,
                                     related_name='nacionalidad',
                                     verbose_name='Nacionalidad')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE,
                                   related_name='usuario',
                                   verbose_name='Usuario',
                                   primary_key=True)
    foto = models.ForeignKey(Fotos, related_name='foto_perfil',
                             on_delete=models.CASCADE)

    def __str__(self):
        first_name = self.usuario.first_name or ''
        last_name = self.usuario.last_name or ''
        return f"{first_name} {last_name}"
