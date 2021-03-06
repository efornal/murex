from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime
import django.dispatch

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    nombre = models.CharField(max_length=200,null=False)
    direccion = models.CharField(max_length=200,null=True, blank=True)
    telefono = models.CharField(max_length=200,null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    
    class Meta:
        db_table = 'proveedores'
        verbose_name_plural = 'Proveedores'

    def __unicode__(self):
        return "%s" % (self.nombre)

    
class Oficina(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    nombre = models.CharField(max_length=200,null=False)
    
    class Meta:
        db_table = 'oficinas'
        verbose_name_plural = 'Oficinas'
        
    def __unicode__(self):
        return "%s" % (self.nombre)

    
class Impresora(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    nombre = models.CharField(max_length=200,null=False)
    oficina = models.ForeignKey(Oficina, null=True, blank=True)
    
    class Meta:
        db_table = 'impresoras'
        verbose_name_plural = 'Impresoras'
        
    def __unicode__(self):
        return "%s" % (self.nombre)

    
class Estado(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    nombre = models.CharField(max_length=200,null=False)
    DADO_DE_BAJA = 6
    
    class Meta:
        db_table = 'estados'
        verbose_name_plural = 'Estados'
        
    def __unicode__(self):
        return "%s" % (self.nombre)


class Toner(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    marca = models.CharField(max_length=200,null=False)
    modelo = models.CharField(max_length=200,null=False)
    identificador = models.CharField(max_length=200,null=False)
    descripcion = models.TextField(null=True, blank=True)
    proveedor = models.ForeignKey(Proveedor, null=True, blank=True)
    impresora = models.ForeignKey(Impresora, null=True, blank=True)
    estados = models.ManyToManyField(Estado, through='EstadoToner')
    recargas  = models.IntegerField(default=0,null=False)
    
    class Meta:
        db_table = 'toners'
        verbose_name_plural = 'Toners'

    def __unicode__(self):
        return "%s" % (self.identificador)

    def estado_actual(self):
        return EstadoToner.objects.filter(toner_id=self.id).order_by('-fecha_inicio')[0]

    def ultimo_estado(self):
        estado_actual = EstadoToner.objects.filter(toner_id=self.id).order_by('-fecha_inicio')[0]
        return Estado.objects.get(id=estado_actual.estado_id)

    def definir_estado(self, nuevo_estado_id):
        estado = self.estado_actual()
        if estado.estado_id == int(nuevo_estado_id):
            return False
        estado.fecha_fin = datetime.now()
        estado_nuevo = EstadoToner(toner_id = self.id,
                                   estado_id = nuevo_estado_id,
                                   fecha_inicio = datetime.now())
        estado_nuevo.save()
        estado.save(update_fields=['fecha_fin'])
        if int(estado_nuevo.estado_id) == 3: # 3 => En stock cargado
            self.recargas += 1
            self.save(update_fields=['recargas'])
        return True

    @classmethod
    def por_estados(cls):
        query = "SELECT t.id, t.identificador,e.estado_id,e.fecha_inicio" \
        " FROM toners as t LEFT OUTER JOIN estados_toners as e ON ( t.id = e.toner_id )" \
        " WHERE e.id = (select id from estados_toners " \
                       "where toner_id = t.id order by fecha_inicio desc limit 1)" \
                       "and e.estado_id != {}" \
        " ORDER BY e.estado_id ASC".format(Estado.DADO_DE_BAJA)
        return cls.objects.raw( query )

    @classmethod
    def por_modelos(cls):
        query = "SELECT * " \
        " FROM toners as t " \
        " WHERE t.id not in (select et.toner_id from estados_toners as et " \
                       "where et.toner_id = t.id " \
                       "and et.estado_id = {})" \
        " ORDER BY modelo, identificador".format(Estado.DADO_DE_BAJA)
        return cls.objects.raw( query )

    @classmethod
    def por_estado(cls, estado_id):
        query = "SELECT t.id, t.identificador,e.estado_id,e.fecha_inicio" \
        " FROM toners as t LEFT OUTER JOIN estados_toners as e ON ( t.id = e.toner_id )" \
        " WHERE e.id = (select id from estados_toners " \
                       "where toner_id = t.id  order by fecha_inicio desc limit 1)" \
                " AND e.estado_id = %s " \
        " ORDER BY e.estado_id ASC" % (estado_id)
        return cls.objects.raw( query )

    @classmethod
    def por_proveedor(cls, proveedor_id):
        query = "SELECT * " \
        " FROM toners as t INNER JOIN proveedores as p on ( t.proveedor_id = p.id )" \
        " WHERE t.id not in (select et.toner_id from estados_toners as et " \
                       "where et.toner_id = t.id " \
                       "and et.estado_id = {}) " \
                       "and p.id = {} " \
        " ORDER BY p.nombre ".format(Estado.DADO_DE_BAJA, proveedor_id)
        return cls.objects.raw( query )

    
@receiver(post_save, sender=Toner)
def estado_inicial(sender, instance, **kwargs):
    if kwargs['created']:
        estado = EstadoToner(toner_id=instance.id, estado_id=3, fecha_inicio=datetime.now())
        estado.save()

    
     
class EstadoToner(models.Model):
    estado = models.ForeignKey(Estado)
    toner  = models.ForeignKey(Toner)
    fecha_inicio = models.DateTimeField(null=False)
    fecha_fin = models.DateTimeField(null=True, blank=True)
    recargado = models.BooleanField(default=False,null=False)
 
    class Meta:
        db_table = 'estados_toners'
        verbose_name_plural = 'EstadosToners'
        
    def __unicode__(self):
        return "%s" % (self.toner.identificador)

    def fue_recargado(self):
        return self.recargado

