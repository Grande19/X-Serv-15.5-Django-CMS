from django.shortcuts import render
from django.http import HttpResponse
from models import Pages

# Create your views here.
def id (request , identificador ):
    try :
        pg = Pages.objects.get(id = int(identificador)) #me muestra el id
        pag = str(pg.page)
        return HttpResponse ('<h1>Todo correcto<h2>')
    except Pages.DoesNotExist :
        respuesta = ("<h1>Error . No hay pagina para este identificador </h1>")
        return HttpResponse(respuesta)

def recurso (request , recurso) :
    try :
        pg = Pages.objects.get(name = recurso)
        pag = str(pg.page)
        return HttpResponse ('<h1>Todo correcto<h2>')
    except Pages.DoesNotExist :
        return HttpResponse ('Error . No hay pagina para el recurso introducido')
