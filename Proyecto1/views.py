from typing import ContextManager
from django.http import HttpResponse
import datetime
from django.template import Template, Context

# A cada función que creemos aquí, le denominamos vista
class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

# Primera vista
def saludo(request):
    
    #Creo una variable
    nombre="Manolito"
    apellido="Cyberchorbo"
    p1=Persona("Alumno manolito","cyberchorbo")
    
    # Paso de objetos
    objeto=datetime.datetime.now() #Almaceno la fecha y hora del sistema


    #Plantillas
    doc_externo=open("C:/Users/manue/OneDrive - UNED/Proyectos_django/Proyecto1/Proyecto1/plantillas_django/miplantilla.html")
    
    #Creamos el objeto template
    plt=Template(doc_externo.read())
    doc_externo.close()

    #Creamos el contexto desde el que pasamos variables y objetos a las plantillas
    ctx=Context({"objeto_date":objeto, "nombre_persona":p1.nombre, "Apellido_persona":p1.apellido, "valor":" esto es un valor"}) # los valores de las variables las pasamos en forma de diccionario
                                                                        # podemos poner el valor directamente entrecomillado
    documento=plt.render(ctx)

    return HttpResponse(documento)

def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    documento=""" <html>
    <body>
    <h1>
    La fecha y hora actuales del sistema son: %s
    </h1>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

#Esta vista recibe el año y nos calcula la edad que tendremos en el.
#Esta vista recibe dos parámetros
def calculaEdad(request, ano): 
    edadActual=18 # la edad inicial será fija
    periodo=ano-2021
    edadFutura=edadActual+periodo
    documento="""<html>
    <body>
    <h1>
    En el año %s tendrás %s años""" %(ano,edadFutura) 
    """</h1>
    </body>
    </html>"""
    return(HttpResponse(documento))

#Esta vista recibe tres parámetros
def calculaEdad2(request, edad, ano): 
    periodo=ano-2021
    edadFutura=edad+periodo
    documento="""<html>
    <body>
    <h1>
    En el año %s tendrás %s años""" %(ano,edadFutura) 
    """</h1>
    </body>
    </html>"""
    return(HttpResponse(documento))