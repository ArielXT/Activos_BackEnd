from random import choice, choices
from rest_framework import serializers
from .models import *

class Loc_EmpresaSerializer(serializers.Serializer):
    class Meta:
        model = Loc_Empresa
        fields = {'id_locempresa','nom_empresa','ruc'}
    
    id_locempresa = serializers.CharField(max_length=50)
    nom_empresa = serializers.CharField(max_length=100)
    ruc = serializers.IntegerField()

    def create(self, validated_data):
        return Loc_Empresa.objects.create(**validated_data)    
    def update(self,instance,validated_data):
        instance.id_locempresa = validated_data.get('id_locempresa',instance.id_locempresa)
        instance.nom_empresa = validated_data.get('nom_empresa',instance.nom_empresa)
        instance.ruc = validated_data.get('ruc',instance.ruc)
        instance.save()
        return instance

class SedeSerializer(serializers.Serializer):
    class Meta:
        model = Sede
        fields = {'id_sede','nombre','direccion'}
    
    id_sede = serializers.CharField(max_length=50)
    nombre = serializers.CharField(max_length=100)
    direccion = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Sede.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.id_sede = validated_data.get('id_sede',instance.id_sede)
        instance.nombre = validated_data.get('nombre',instance.nombre)
        instance.direccion = validated_data.get('direccion',instance.direccion)
        instance.save()
        return instance

class Centro_de_costeSerializer(serializers.Serializer):
    class Meta:
        model = Centro_de_coste
        fields = {'id_ceco','descripcion'}
    
    id_ceco = serializers.CharField(max_length=50)
    descripcion = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Centro_de_coste.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.id_ceco = validated_data.get('id_ceco',instance.id_ceco)
        instance.descripcion = validated_data.get('descripcion',instance.descripcion)
        instance.save()
        return instance

class EmpleadoSerializer(serializers.Serializer):
    class Meta:
        model = Empleado
        fields = {'dni','nombre','apellido','area','id_locempresa','cargo','id_sede','id_ceco'}
    
    dni = serializers.IntegerField()
    nombre = serializers.CharField(max_length=100)
    apellido = serializers.CharField(max_length=100)
    area = serializers.CharField(max_length=100)
    id_locempresa = serializers.SlugRelatedField(queryset=Loc_Empresa.objects.all(), slug_field='id_locempresa')
    cargo = serializers.CharField(max_length=50)
    id_sede = serializers.SlugRelatedField(queryset=Sede.objects.all(), slug_field='id_sede')
    id_ceco = serializers.SlugRelatedField(queryset=Centro_de_coste.objects.all(), slug_field='id_ceco')

    def to_representation(self, instance):
                rep = super(EmpleadoSerializer, self).to_representation(instance)
                rep['id_locempresa'] = instance.id_locempresa.nom_empresa
                rep['id_sede'] = instance.id_sede.nombre
                rep['id_ceco'] = instance.id_ceco.descripcion
                return rep

    def create(self, validated_data):
        return Empleado.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.dni = validated_data.get('dni',instance.dni)
        instance.nombre = validated_data.get('nombre',instance.nombre)
        instance.apellido = validated_data.get('apellido',instance.apellido)
        instance.area = validated_data.get('area',instance.area)
        instance.id_locempresa = validated_data.get('id_locempresa',instance.id_locempresa)
        instance.cargo = validated_data.get('cargo',instance.cargo)
        instance.id_sede = validated_data.get('id_sede',instance.id_sede)
        instance.id_ceco = validated_data.get('id_ceco',instance.id_ceco)
        instance.save()
        return instance

class TipoSerializer(serializers.Serializer):
    class Meta:
        model = Tipo
        fields = {'id_tipo','descripcion'}
    
    id_tipo = serializers.IntegerField()
    descripcion = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Tipo.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.id_tipo = validated_data.get('id_tipo',instance.id_tipo)
        instance.descripcion = validated_data.get('descripcion',instance.descripcion)
        instance.save()
        return instance

class AdministradorSerializer(serializers.Serializer):
    class Meta:
        model = Administrador
        fields = {'id_admin','dni','estado','iniciales'}
    
    id_admin = serializers.IntegerField()
    dni = serializers.SlugRelatedField(queryset=Empleado.objects.all(), slug_field='dni')
    estado = serializers.ChoiceField(choices=Administrador.activo_o_no)
    iniciales = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Administrador.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.id_admin = validated_data.get('id_admin',instance.id_admin)
        instance.dni = validated_data.get('dni',instance.dni)
        instance.estado = validated_data.get('estado',instance.estado)
        instance.iniciales = validated_data.get('iniciales',instance.iniciales)
        instance.save()
        return instance

class Nivel_AccesoSerializer(serializers.Serializer):
    class Meta:
        model = Nivel_Acceso
        fields = {'id_nivelacceso','id_admin','id_tipo','estado'}
    
    id_nivelacceso = serializers.IntegerField()
    id_admin = serializers.SlugRelatedField(queryset=Administrador.objects.all(), slug_field='id_admin')
    id_tipo = serializers.SlugRelatedField(queryset=Tipo.objects.all(), slug_field='id_tipo')
    estado = serializers.ChoiceField(choices=Administrador.activo_o_no)

    def to_representation(self, instance):
            rep = super(Nivel_AccesoSerializer, self).to_representation(instance)
            rep['id_admin'] = instance.id_admin.iniciales
            rep['id_tipo'] = instance.id_tipo.descripcion
            return rep

    def create(self, validated_data):
        return Nivel_Acceso.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.id_nivelacceso = validated_data.get('id_nivelacceso',instance.id_nivelacceso)
        instance.id_admin = validated_data.get('id_admin',instance.id_admin)
        instance.id_tipo = validated_data.get('id_tipo',instance.id_tipo)
        instance.estado = validated_data.get('estado',instance.estado)
        instance.save()
        return instance

class Activo_TISerializer(serializers.Serializer):
    class Meta:
        model = Activo_TI
        fields = {'id','nombre','hostname','ip_interna','ip_externa','id_tipo','usuario','clave','link','observacion',
        'rol_servicio','clin_empresa','tipo','f_inicio','f_final','estado','descripcion','fabricante','marca'}
    
    id = serializers.IntegerField()
    nombre = serializers.CharField(max_length=100)
    hostname = serializers.CharField(max_length=100)
    ip_interna = serializers.CharField(max_length=100)
    ip_externa = serializers.CharField(max_length=100)
    id_tipo = serializers.SlugRelatedField(queryset=Tipo.objects.all(), slug_field='id_tipo')
    usuario = serializers.CharField(max_length=50)
    clave = serializers.CharField(max_length=25)
    link = serializers.CharField(max_length=100)
    observacion = serializers.CharField(max_length=100)
    rol_servicio = serializers.CharField(max_length=100)
    clin_empresa = serializers.CharField(max_length=100)
    tipo = serializers.CharField(max_length=100)
    f_inicio = serializers.DateField()
    f_final = serializers.DateField()
    estado = serializers.ChoiceField(choices=Activo_TI.activo_o_no)
    descripcion = serializers.CharField(max_length=100)
    fabricante = serializers.CharField(max_length=100)
    marca = serializers.CharField(max_length=100)

    def to_representation(self, instance):
                rep = super(Activo_TISerializer, self).to_representation(instance)
                rep['id_tipo'] = instance.id_tipo.descripcion
                return rep
                
    def create(self, validated_data):
        return Activo_TI.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.id = validated_data.get('id',instance.id)
        instance.nombre = validated_data.get('nombre',instance.nombre)
        instance.hostname = validated_data.get('hostname',instance.hostname)
        instance.ip_interna = validated_data.get('ip_interna',instance.ip_interna)
        instance.ip_externa = validated_data.get('ip_externa',instance.ip_externa)
        instance.id_tipo = validated_data.get('id_tipo',instance.id_tipo)
        instance.usuario = validated_data.get('usuario',instance.usuario)
        instance.clave = validated_data.get('clave',instance.clave)
        instance.link = validated_data.get('link',instance.link)
        instance.observacion = validated_data.get('observacion',instance.observacion)
        instance.rol_servicio = validated_data.get('rol_servicio',instance.rol_servicio)
        instance.clin_empresa = validated_data.get('clin_empresa',instance.clin_empresa)
        instance.tipo = validated_data.get('tipo',instance.tipo)
        instance.f_inicio = validated_data.get('f_inicio',instance.f_inicio)
        instance.f_final = validated_data.get('f_final',instance.f_final)
        instance.estado = validated_data.get('estado',instance.estado)
        instance.descripcion = validated_data.get('descripcion',instance.descripcion)
        instance.fabricante = validated_data.get('fabricante',instance.fabricante)
        instance.marca = validated_data.get('marca',instance.marca)
        instance.save()
        return instance

class ProveedorSerializer(serializers.Serializer):
    class Meta:
        model = Proveedor
        fields = {'id_proveedor','ruc','nombre'}
    
    id_proveedor = serializers.IntegerField()
    ruc = serializers.IntegerField()
    nombre = serializers.CharField(max_length=100)
    

    def create(self, validated_data):
        return Proveedor.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.id_proveedor = validated_data.get('id_proveedor',instance.id_proveedor)
        instance.ruc = validated_data.get('ruc',instance.ruc)
        instance.nombre = validated_data.get('nombre',instance.nombre)
        
        instance.save()
        return instance

class ServicioSerializer(serializers.Serializer):
    class Meta:
        model = Servicio
        fields = {'id_servicio','nombre_cor','nombre_larg'}
    
    id_servicio = serializers.IntegerField()
    nombre_cor = serializers.CharField(max_length=50)
    nombre_larg = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Servicio.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.id_servicio = validated_data.get('id_servicio',instance.id_servicio)
        instance.nombre_cor = validated_data.get('nombre_cor',instance.nombre_cor)
        instance.nombre_larg = validated_data.get('nombre_larg',instance.nombre_larg)
        instance.save()
        return instance

class Prov_ServicioSerializer(serializers.Serializer):
    class Meta:
        model = Prov_Servicio
        fields = {'id_provservicio','id_proveedor','id_servicio','nombre'}
    
    id_provservicio = serializers.IntegerField()
    id_proveedor = serializers.SlugRelatedField(queryset=Proveedor.objects.all(), slug_field='id_proveedor')
    id_servicio = serializers.SlugRelatedField(queryset=Servicio.objects.all(), slug_field='id_servicio')
    nombre = serializers.CharField(max_length=100)

    def to_representation(self, instance):
                rep = super(Prov_ServicioSerializer, self).to_representation(instance)
                rep['id_proveedor'] = instance.id_proveedor.nombre
                rep['id_servicio'] = instance.id_servicio.nombre_larg
                return rep

    def create(self, validated_data):
        return Prov_Servicio.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.id_provservicio = validated_data.get('id_provservicio',instance.id_provservicio)
        instance.id_proveedor = validated_data.get('id_proveedor',instance.id_proveedor)
        instance.id_servicio = validated_data.get('id_servicio',instance.id_servicio)
        instance.nombre = validated_data.get('nombre',instance.nombre)
        instance.save()
        return instance

class Activo_provSerializer(serializers.Serializer):
    class Meta:
        model = Activo_prov
        fields = {'id_actprov','id','id_provservicio'}
    
    id_actprov = serializers.IntegerField()
    id = serializers.SlugRelatedField(queryset=Activo_TI.objects.all(), slug_field='id')
    id_provservicio = serializers.SlugRelatedField(queryset=Prov_Servicio.objects.all(), slug_field='id_provservicio')

    def to_representation(self, instance):
                rep = super(Activo_provSerializer, self).to_representation(instance)
                rep['id'] = instance.id.nombre
                rep['id_provservicio'] = instance.id_provservicio.nombre
                return rep

    def create(self, validated_data):
        return Activo_prov.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.id_actprov = validated_data.get('id_actprov',instance.id_actprov)
        instance.id = validated_data.get('id',instance.id)
        instance.id_provservicio = validated_data.get('id_provservicio',instance.id_provservicio)
        instance.save()
        return instance

class EmpresaSerializer(serializers.Serializer):
    class Meta:
        model = Empresa
        fields = {'id_empresa','descripcion','ruc'}
    id_empresa = serializers.IntegerField()
    descripcion = serializers.CharField(max_length=100)
    ruc = serializers.IntegerField()

    def create(self, validated_data):
        return Empresa.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.id_empresa = validated_data.get('id_empresa',instance.id_empresa)
        instance.descripcion = validated_data.get('descripcion',instance.descripcion)
        instance.ruc = validated_data.get('ruc',instance.ruc)
        instance.save()
        return instance

class ContratoSerializer(serializers.Serializer):
    class Meta:
        model = Contrato
        fields = {'id_contrato','id_proveedor','id_empresa','f_firma','estado','nombre','f_final'}
    id_contrato = serializers.IntegerField()
    id_proveedor = serializers.SlugRelatedField(queryset=Proveedor.objects.all(), slug_field='id_proveedor')
    id_empresa = serializers.SlugRelatedField(queryset=Empresa.objects.all(), slug_field='id_empresa')
    f_firma = serializers.DateField()
    estado = serializers.ChoiceField(choices=Contrato.activo_o_no)
    nombre = serializers.CharField(max_length=100)
    f_final = serializers.DateField()

    def to_representation(self, instance):
        rep = super(ContratoSerializer, self).to_representation(instance)
        rep['id_empresa'] = instance.id_empresa.descripcion
        rep['id_proveedor'] = instance.id_proveedor.nombre
        return rep

    def create(self, validated_data):
        return Contrato.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.id_contrato = validated_data.get('id_contrato',instance.id_contrato)
        instance.id_proveedor = validated_data.get('id_proveedor',instance.id_proveedor)
        instance.id_empresa = validated_data.get('id_empresa',instance.id_empresa)
        instance.f_firma = validated_data.get('f_firma',instance.f_firma)
        instance.estado = validated_data.get('estado',instance.estado)
        instance.nombre = validated_data.get('nombre',instance.nombre)
        instance.f_final = validated_data.get('f_final',instance.f_final)
        instance.save()
        return instance

class Activo_contratoSerializer(serializers.Serializer):
    class Meta:
        model = Activo_contrato
        fields = {'id_actcontrato','id','id_contrato'}
    
    id_actcontrato = serializers.IntegerField()
    id = serializers.SlugRelatedField(queryset=Activo_TI.objects.all(), slug_field='id')
    id_contrato = serializers.SlugRelatedField(queryset=Contrato.objects.all(), slug_field='id_contrato')

    def to_representation(self, instance):
        rep = super(Activo_contratoSerializer, self).to_representation(instance)
        rep['id'] = instance.id.nombre
        rep['id_contrato'] = instance.id_contrato.nombre
        return rep

    def create(self, validated_data):
        return Activo_contrato.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.id_actcontrato = validated_data.get('id_actcontrato',instance.id_actcontrato)
        instance.id = validated_data.get('id',instance.id)
        instance.id_contrato = validated_data.get('id_contrato',instance.id_contrato)
        instance.save()
        return instance

class Activo_empleadoSerializer(serializers.Serializer):
    class Meta:
        model = Activo_empleado
        fields = {'id_actempleado','dni','id','estado','f_inicio','f_fin'}
    
    id_actempleado = serializers.IntegerField()    
    dni = serializers.SlugRelatedField(queryset=Empleado.objects.all(), slug_field='dni')
    id = serializers.SlugRelatedField(queryset=Activo_TI.objects.all(), slug_field='id')
    estado = serializers.ChoiceField(choices=Activo_empleado.activo_o_no)
    f_inicio = serializers.DateField()
    f_fin = serializers.DateField()

    def to_representation(self, instance):
        rep = super(Activo_empleadoSerializer, self).to_representation(instance)
        rep['id'] = instance.id.nombre
        return rep

    def create(self, validated_data):
        return Activo_empleado.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.id_actempleado = validated_data.get('id_actempleado',instance.id_actempleado)
        instance.dni = validated_data.get('dni',instance.dni)
        instance.id = validated_data.get('id',instance.id)
        instance.estado = validated_data.get('estado',instance.estado)
        instance.f_inicio = validated_data.get('f_inicio',instance.f_inicio)
        instance.f_fin = validated_data.get('f_fin',instance.f_fin)
        instance.save()
        return instance