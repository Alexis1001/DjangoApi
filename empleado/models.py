from django.db import models

#usuario
class Negocio(models.Model):
    name   = models.CharField(max_length=50, blank=True)
    state  = models.CharField(max_length=50, blank=True)
    status = models.IntegerField(default=0)
    class Meta:
        db_table = 'negocios'
     
#denuncias        
class Empleado(models.Model):
    name   = models.CharField(max_length=50, blank=True)
    state  = models.CharField(max_length=50, blank=True)
    re_negocio = models.ForeignKey(Negocio, related_name='empleados', on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    class Meta:
        db_table = 'empleados'
