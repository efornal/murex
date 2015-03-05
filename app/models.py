from django.db import models


class Proveedor(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    nombre = models.CharField(max_length=200,null=False)
    direccion = models.CharField(max_length=200,null=False)
    telefono = models.CharField(max_length=200,null=False)
    descripcion = models.TextField(null=True)
    
    class Meta:
        db_table = 'proveedores'
        verbose_name_plural = 'Preoveedores'
        
    def __str__(self):
        return self.nombre

    
class Impresora(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    nombre = models.CharField(max_length=200,null=False)
    
    class Meta:
        db_table = 'impresoras'
        verbose_name_plural = 'Impresoras'
        
    def __str__(self):
        return self.nombre

    
class Estado(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    nombre = models.CharField(max_length=200,null=False)
    
    class Meta:
        db_table = 'estados'
        verbose_name_plural = 'Estados'
        
    def __str__(self):
        return self.nombre

    
class Toner(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    marca = models.CharField(max_length=200,null=False)
    modelo = models.CharField(max_length=200,null=False)
    identificador = models.CharField(max_length=200,null=False)
    proveedor = models.ForeignKey(Proveedor, null=True)
    impresora = models.ForeignKey(Impresora, null=True)
    estados = models.ManyToManyField(Estado, through='EstadoToner')
    
    class Meta:
        db_table = 'toners'
        verbose_name_plural = 'Toners'
        
    def __str__(self):
        return self.nombre

    
class EstadoToner(models.Model):
    estado = models.ForeignKey(Estado)
    toner = models.ForeignKey(Toner)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    recargado = models.BooleanField(default=False)
 
    class Meta:
        db_table = 'estados_toners'
        verbose_name_plural = 'EstadosToners'
        
    def __str__(self):
        return self.nombre
