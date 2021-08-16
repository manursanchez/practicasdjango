from django.http import HttpResponse
import datetime

# A cada función que creemos aquí, le denominamos vista

# Primera vista
def saludo(request):
    documento=""" <html>
    <body>
    <h1>
    Hola Manolito
    </h1>
    </body>
    </html>"""
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