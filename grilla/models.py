from django.db import models

# Create your models here.
from django.db import models


class Liquidacion(models.Model):
 # id = models.PositiveIntegerField()
    documento = models.CharField(max_length=8)
    nombre = models.CharField(max_length=145)
    fecha_liquidacion = models.DateField()
    programa_id = models.PositiveIntegerField()
    jerarquia_id = models.PositiveIntegerField()
    agrupacion_id = models.PositiveIntegerField()
    codigo = models.PositiveIntegerField()
    monto = models.FloatField()
    tipo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'liquidacion'
