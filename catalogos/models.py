from django.db import models


# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=3)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paises'


class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(verbose_name='descripción')
    foto = models.ImageField(verbose_name='imagen', upload_to='cursos/fotos')
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Fotos(models.Model):
    imagen = models.ImageField(upload_to='cursos/fotos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tema(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='temas_curso')
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(verbose_name='descripción')
    fotos = models.ManyToManyField(Fotos, related_name='fotos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
