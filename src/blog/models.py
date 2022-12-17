from django.db import models
from django.utils import timezone
#modelo para el Post en el blog

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion =models.TextField()
    fecha_creacion = models.DateField(default=timezone.now)
    fecha_publicacion = models.DateField(default=timezone.now)

