from django.db import models
from django.utils.timezone import now
class Tarea(models.Model):
    titulo          = models.CharField(max_length=200)
    descripcion     = models.CharField(blank= True, max_length = 200)
    fecha_creacion  = models.DateTimeField(default=now)
    fecha_limite    = models.DateTimeField(null= True)
    prioridad       = models.CharField(max_length=5)
    

