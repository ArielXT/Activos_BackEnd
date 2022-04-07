from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

# Create your views here.
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

#------------------------------------------------
@csrf_exempt
def loc_empresa_list(request):
    if request.method == 'GET':
        loc_empresa = Loc_Empresa.objects.all()
        serializer = Loc_EmpresaSerializer(loc_empresa, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Loc_EmpresaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
@csrf_exempt
def loc_empresa_detail(request, pk):
    try:
        loc_empresa = Loc_Empresa.objects.get(pk=pk)
    except Loc_Empresa.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = Loc_EmpresaSerializer(loc_empresa)
        return JSONResponse(serializer.data)    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Loc_EmpresaSerializer(loc_empresa, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        loc_empresa.delete()
    return HttpResponse(status=204)
#--------------------------------------------------------------------
@csrf_exempt
def sede_list(request):
    if request.method == 'GET':
        sede = Sede.objects.all()
        serializer = SedeSerializer(sede, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SedeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
@csrf_exempt
def sede_detail(request, pk):
    try:
        sede = Sede.objects.get(pk=pk)
    except Sede.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = SedeSerializer(sede)
        return JSONResponse(serializer.data)    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SedeSerializer(sede, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        sede.delete()
    return HttpResponse(status=204)
#--------------------------------------------------------------------
@csrf_exempt
def centro_de_coste_list(request):
    if request.method == 'GET':
        ccoste = Centro_de_coste.objects.all()
        serializer = Centro_de_costeSerializer(ccoste, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Centro_de_costeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
@csrf_exempt
def centro_de_coste_detail(request, pk):
    try:
        ccoste = Centro_de_coste.objects.get(pk=pk)
    except Centro_de_coste.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = Centro_de_costeSerializer(ccoste)
        return JSONResponse(serializer.data)    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Centro_de_costeSerializer(ccoste, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        ccoste.delete()
    return HttpResponse(status=204)
#--------------------------------------------------------------------
@csrf_exempt
def empleado_list(request):
    if request.method == 'GET':
        empleado = Empleado.objects.all()
        serializer = EmpleadoSerializer(empleado, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmpleadoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
@csrf_exempt
def empleado_detail(request, pk):
    try:
        empleado = Empleado.objects.get(pk=pk)
    except Empleado.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = EmpleadoSerializer(empleado)
        return JSONResponse(serializer.data)    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EmpleadoSerializer(empleado, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        empleado.delete()
    return HttpResponse(status=204)
#--------------------------------------------------------------------
@csrf_exempt
def activo_empleado_list(request):
    if request.method == 'GET':
        actempleado = Activo_empleado.objects.all()
        serializer = Activo_empleadoSerializer(actempleado, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Activo_empleadoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
@csrf_exempt
def activo_empleado_detail(request, pk):
    try:
        actempleado = Activo_empleado.objects.get(pk=pk)
    except Activo_empleado.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = Activo_empleadoSerializer(actempleado)
        return JSONResponse(serializer.data)    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Activo_empleadoSerializer(actempleado, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        actempleado.delete()
    return HttpResponse(status=204)
#--------------------------------------------------------------------
@csrf_exempt
def administrador_list(request):
    if request.method == 'GET':
        administrador = Administrador.objects.all()
        serializer = AdministradorSerializer(administrador, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AdministradorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
@csrf_exempt
def administrador_detail(request, pk):
    try:
        administrador = Administrador.objects.get(pk=pk)
    except Administrador.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = AdministradorSerializer(administrador)
        return JSONResponse(serializer.data)    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AdministradorSerializer(administrador, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        administrador.delete()
    return HttpResponse(status=204)
#--------------------------------------------------------------------
@csrf_exempt
def nivel_acceso_list(request):
    if request.method == 'GET':
        nacceso = Nivel_Acceso.objects.all()
        serializer = Nivel_AccesoSerializer(nacceso, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Nivel_AccesoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
@csrf_exempt
def nivel_acceso_detail(request, pk):
    try:
        nacceso = Nivel_Acceso.objects.get(pk=pk)
    except Nivel_Acceso.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = Nivel_AccesoSerializer(nacceso)
        return JSONResponse(serializer.data)    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Nivel_AccesoSerializer(nacceso, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        nacceso.delete()
    return HttpResponse(status=204)
#--------------------------------------------------------------------
@csrf_exempt
def tipo_list(request):
    if request.method == 'GET':
        tipo = Tipo.objects.all()
        serializer = TipoSerializer(tipo, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TipoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
@csrf_exempt
def tipo_detail(request, pk):
    try:
        tipo = Tipo.objects.get(pk=pk)
    except Tipo.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = TipoSerializer(tipo)
        return JSONResponse(serializer.data)    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TipoSerializer(tipo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        tipo.delete()
    return HttpResponse(status=204)
#--------------------------------------------------------------------
@csrf_exempt
def activo_ti_list(request):
    if request.method == 'GET':
        activoti = Activo_TI.objects.all()
        serializer = Activo_TISerializer(activoti, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Activo_TISerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
@csrf_exempt
def activo_ti_detail(request, pk):
    try:
        activoti = Activo_TI.objects.get(pk=pk)
    except Activo_TI.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = Activo_TISerializer(activoti)
        return JSONResponse(serializer.data)    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Activo_TISerializer(activoti, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        activoti.delete()
    return HttpResponse(status=204)
#--------------------------------------------------------------------
@csrf_exempt
def activo_prov_list(request):
    if request.method == 'GET':
        activoprov = Activo_prov.objects.all()
        serializer = Activo_provSerializer(activoprov, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Activo_provSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
@csrf_exempt
def activo_prov_detail(request, pk):
    try:
        activoprov = Activo_prov.objects.get(pk=pk)
    except Activo_prov.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = Activo_provSerializer(activoprov)
        return JSONResponse(serializer.data)    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Activo_provSerializer(activoprov, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        activoprov.delete()
    return HttpResponse(status=204)
#--------------------------------------------------------------------
@csrf_exempt
def prov_servicio_list(request):
    if request.method == 'GET':
        provservice = Prov_Servicio.objects.all()
        serializer = Prov_ServicioSerializer(provservice, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Prov_ServicioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
@csrf_exempt
def prov_servicio_detail(request, pk):
    try:
        provservice = Prov_Servicio.objects.get(pk=pk)
    except Prov_Servicio.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = Prov_ServicioSerializer(provservice)
        return JSONResponse(serializer.data)    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Prov_ServicioSerializer(provservice, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        provservice.delete()
    return HttpResponse(status=204)
#--------------------------------------------------------------------
@csrf_exempt
def proveedor_list(request):
    if request.method == 'GET':
        proveedor = Proveedor.objects.all()
        serializer = ProveedorSerializer(proveedor, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProveedorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
@csrf_exempt
def proveedor_detail(request, pk):
    try:
        proveedor = Proveedor.objects.get(pk=pk)
    except Proveedor.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ProveedorSerializer(proveedor)
        return JSONResponse(serializer.data)    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProveedorSerializer(proveedor, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        proveedor.delete()
    return HttpResponse(status=204)

#--------------------------------------------------------------------
@csrf_exempt
def servicio_list(request):
    if request.method == 'GET':
        service = Servicio.objects.all()
        serializer = ServicioSerializer(service, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ServicioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
@csrf_exempt
def servicio_detail(request, pk):
    try:
        service = Servicio.objects.get(pk=pk)
    except Servicio.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ServicioSerializer(service)
        return JSONResponse(serializer.data)    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ServicioSerializer(service, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        service.delete()
    return HttpResponse(status=204)
#--------------------------------------------------------------------
@csrf_exempt
def empresa_list(request):
    if request.method == 'GET':
        empresa = Empresa.objects.all()
        serializer = EmpresaSerializer(empresa, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmpresaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
@csrf_exempt
def empresa_detail(request, pk):
    try:
        empresa = Empresa.objects.get(pk=pk)
    except Empresa.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = EmpresaSerializer(empresa)
        return JSONResponse(serializer.data)    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EmpresaSerializer(empresa, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        empresa.delete()
    return HttpResponse(status=204)
#--------------------------------------------------------------------
@csrf_exempt
def contrato_list(request):
    if request.method == 'GET':
        contrato = Contrato.objects.all()
        serializer = ContratoSerializer(contrato, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ContratoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
@csrf_exempt
def contrato_detail(request, pk):
    try:
        contrato = Contrato.objects.get(pk=pk)
    except Contrato.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ContratoSerializer(contrato)
        return JSONResponse(serializer.data)    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ContratoSerializer(contrato, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        contrato.delete()
    return HttpResponse(status=204)
#--------------------------------------------------------------------
@csrf_exempt
def activo_contrato_list(request):
    if request.method == 'GET':
        acontrato = Activo_contrato.objects.all()
        serializer = Activo_contratoSerializer(acontrato, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Activo_contratoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
@csrf_exempt
def activo_contrato_detail(request, pk):
    try:
        acontrato = Activo_contrato.objects.get(pk=pk)
    except Activo_contrato.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = Activo_contratoSerializer(acontrato)
        return JSONResponse(serializer.data)    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Activo_contratoSerializer(acontrato, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        acontrato.delete()
    return HttpResponse(status=204)