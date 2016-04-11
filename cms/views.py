from django.shortcuts import render
from django.http import HttpResponse
from models import Pages

# Create your views here.
def id (request , identificador ):
    try :
        pages = Pages.objects.get(id = int(identificador)) #me muestra el id
        pag = str(pages.page)
        return HttpResponse ('<h1>Todo correcto<h2>'+ str(pages))
    except Pages.DoesNotExist :
        respuesta = ("<h1>Error . No hay pagina para este identificador </h1>")
        return HttpResponse(respuesta)

def recurs (request , recurso) :
    try :
        pages = Pages.objects.get(name = recurso)
        return HttpResponse ('<h1>Todo correcto<h2> ' + str(name))
    except Pages.DoesNotExist :
        return HttpResponse ('Error . No hay pagina para el recurso introducido')
