from django.db import models


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
    proveedor = models.ForeignKey(Proveedor, null=True, blank=True)
    impresora = models.ForeignKey(Impresora, null=True, blank=True)
    estados = models.ManyToManyField(Estado, through='EstadoToner')
    
    class Meta:
        db_table = 'toners'
        verbose_name_plural = 'Toners'

    def __unicode__(self):
        return "%s" % (self.identificador)

     
class EstadoToner(models.Model):
    estado = models.ForeignKey(Estado)
    toner  = models.ForeignKey(Toner)
    fecha_inicio = models.DateField(null=False)
    fecha_fin = models.DateField(null=True, blank=True)
    recargado = models.BooleanField(default=False,null=False)
 
    class Meta:
        db_table = 'estados_toners'
        verbose_name_plural = 'EstadosToners'

    def __unicode__(self):
        return "%s" % (self.toner.identificador)

