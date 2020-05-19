
# Create your models here.
from django.db import models
import uuid

class Measure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cedula = models.IntegerField(verbose_name='cedula',default=1)
    nombre = models.CharField(verbose_name='nombre', max_length=20,default='1')
    actividad = models.CharField(verbose_name='actividad',max_length=20,default='1')
    estrato = models.CharField(verbose_name='estrato',max_length=2,default='1')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

