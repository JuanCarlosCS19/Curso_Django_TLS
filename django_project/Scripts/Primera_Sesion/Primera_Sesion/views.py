from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Mundo")

def adulto(request,edad):
    if edad >= 18:
        return HttpResponse(f"Eres mayor de edad porque tienes {edad} años")
    else:
        return HttpResponse(f"No eres mayor de edad porque tienes {edad} años")