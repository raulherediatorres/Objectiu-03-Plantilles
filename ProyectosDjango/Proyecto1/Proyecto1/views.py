from django.http import HttpResponse
import datetime
from django.template import Template, Context

#class Persona(object):
    
    
def saludo(request): 
    
    nombre="Juan"
    
    apellido="Díaz"
    
    ahora=fecha_actual=datetime.datetime.now
    
    doc_externo=open("C:/Users/Administrator/Desktop/ProyectosDjango/Proyecto1/Proyecto1/plantillas/miplantilla.html")
    
    plt=Template(doc_externo.read())
    
    doc_externo.close()
    
    ctx=Context({"nombre_persona":nombre, "apellido_persona":apellido, "momento_actual":ahora})
    
    documento=plt.render(ctx)
    
    return HttpResponse(documento)

def habitant(request): 
    
    nombre="Raúl"
    
    apellido="Heredia Torres"
    
    anydenaixement="2004"
    
    ciudad="Badalona"
    
    ciclos=["MP6.Desenvolupament web en entorn client", "MP7.Desenvolupament web d'entorn servidor", "MP8.Desplegamnent d'aplicacions web", "MP9.Disseny d'interfícies web", "MP12.Projecte"] 
    
    ahora=datetime.datetime.now
    
    doc_externo=open("C:/Users/Administrator/Desktop/ProyectosDjango/Proyecto1/Proyecto1/plantillas/miplantilla.html")
    
    plt=Template(doc_externo.read())
    
    doc_externo.close()
    
    ctx=Context({"nombre_persona":nombre, "apellido_persona":apellido, "anyo_nacimiento":anydenaixement, "ciudad":ciudad, "ahora":ahora, "ciclos":ciclos})
    
    documento=plt.render(ctx)
    
    return HttpResponse(documento)

class Alumne(object):
    
    def __init__(self, nombre, apellido, edad, ciudad):
        
        self.nombre=nombre
        
        self.apellido=apellido
        
        self.edad=edad

        self.ciudad=ciudad

def  despedida(request):
    
    return HttpResponse("Hasta luego alumnos de Django")


def dameFecha(request):
    
    fecha_actual=datetime.datetime.now()
    
    documento="""<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" % fecha_actual
    
    return HttpResponse(documento)

def calculaEdad(request,edad, agno):
    
    edadActual=18
    periodo=agno-2023
    edadFutura=edad+periodo
    documento="<html><body><h2>En el año %s tendré %s años" %(agno, edadFutura)
    
    return HttpResponse(documento)

def pagina1(request):
    
    return HttpResponse("Esta es la página 1")

def pagina2(request):
    
    return HttpResponse("Esta es la página 2")

def pagina3(request):
    
    return HttpResponse("Esta es la página 3")

def informacion(request):
    
    fechaHoy=datetime.date.today()
    añoFinal=datetime.date(fechaHoy.year, 12,31)
    diference=(añoFinal-fechaHoy).days
    
    documento="""<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    <br/>
    Fecha y hora hasta el final de año %s
    </h1>
    </body>
    </html>""" % (fechaHoy,diference)
    
    return HttpResponse(documento)

def nombreEdad(request, nombre, anyo):
    
    nombreHoy = nombre
    edadActual = datetime.date.today().year - anyo
    
    documento="""<html>
    <body>
    <h1>
    Tu nombre es %s
    <br/>
    Tienes %s años
    </h1>
    </body>
    </html>""" % (nombreHoy,edadActual)
    
    return HttpResponse(documento)