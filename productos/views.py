from django.http import HttpResponse


def inicio(request):
    return HttpResponse("Bienvenido a la aplicación de Productos")


def informacion(request):
    return HttpResponse("Esta es la página de información de Productos")