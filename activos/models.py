from django.db import models

# Create your models here.
class Loc_Empresa(models.Model):
    id_locempresa = models.CharField(max_length=50,primary_key=True)
    nom_empresa = models.CharField(max_length=100)
    ruc = models.BigIntegerField()

class Sede(models.Model):
    id_sede = models.CharField(max_length=50,primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

class Centro_de_coste(models.Model):
    id_ceco = models.CharField(max_length=50,primary_key=True)
    descripcion = models.CharField(max_length=100)

class Empleado(models.Model):
    dni = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    id_locempresa = models.ForeignKey(Loc_Empresa, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=50)
    id_sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    id_ceco = models.ForeignKey(Centro_de_coste, on_delete=models.CASCADE)

class Tipo(models.Model):
    id_tipo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)

class Administrador(models.Model):
    activo = '1'
    inactivo = '0'
    activo_o_no = [
        (activo, 1),
        (inactivo, 0),
    ]
    id_admin = models.IntegerField(primary_key=True)
    dni = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    estado = models.CharField(max_length=15,choices=activo_o_no,default=activo,)
    iniciales = models.CharField(max_length=50)

class Nivel_Acceso(models.Model):
    activo = '1'
    inactivo = '0'
    activo_o_no = [
        (activo, 1),
        (inactivo, 0),
    ]
    id_nivelacceso = models.IntegerField(primary_key=True)
    id_admin = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    id_tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    estado = models.CharField(max_length=15,choices=activo_o_no,default=activo,)

class Activo_TI(models.Model):
    activo = '1'
    inactivo = '0'
    activo_o_no = [
        (activo, 1),
        (inactivo, 0),
    ]
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    hostname = models.CharField(max_length=100)
    ip_interna = models.CharField(max_length=100)
    ip_externa = models.CharField(max_length=100)
    id_tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=50)
    clave = models.CharField(max_length=25)
    link = models.CharField(max_length=100)
    observacion = models.CharField(max_length=100)
    rol_servicio = models.CharField(max_length=100)
    clin_empresa = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    f_inicio = models.DateField()
    f_final = models.DateField()
    estado = models.CharField(max_length=15,choices=activo_o_no,default=activo,)
    descripcion = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)

class Proveedor(models.Model):
    id_proveedor = models.IntegerField(primary_key=True)
    ruc = models.BigIntegerField()
    nombre = models.CharField(max_length=100)
    
class Servicio(models.Model):
    id_servicio = models.IntegerField(primary_key=True)
    nombre_cor = models.CharField(max_length=50)
    nombre_larg = models.CharField(max_length=100)

class Prov_Servicio(models.Model):
    id_provservicio = models.IntegerField(primary_key=True)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    id_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

class Activo_prov(models.Model):
    id_actprov = models.IntegerField(primary_key=True)
    id = models.ForeignKey(Activo_TI, on_delete=models.CASCADE)
    id_provservicio = models.ForeignKey(Prov_Servicio, on_delete=models.CASCADE)
    
class Empresa(models.Model):
    id_empresa = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    ruc = models.BigIntegerField()

class Contrato(models.Model):
    activo = '1'
    inactivo = '0'
    activo_o_no = [
        (activo, 1),
        (inactivo, 0),
    ]
    id_contrato = models.IntegerField(primary_key=True)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    f_firma = models.DateField()
    estado = models.CharField(max_length=15,choices=activo_o_no,default=activo,)
    nombre = models.CharField(max_length=100)
    f_final = models.DateField()

class Activo_contrato(models.Model):
    id_actcontrato = models.IntegerField(primary_key=True)
    id = models.ForeignKey(Activo_TI, on_delete=models.CASCADE)
    id_contrato = models.ForeignKey(Contrato,on_delete=models.CASCADE)

class Activo_empleado(models.Model):
    activo = '1'
    inactivo = '0'
    activo_o_no = [
        (activo, 1),
        (inactivo, 0),
    ]
    id_actempleado = models.IntegerField(primary_key=True)
    dni = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    id = models.ForeignKey(Activo_TI, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50,choices=activo_o_no,default=activo,)
    f_inicio = models.DateField()
    f_fin = models.DateField()