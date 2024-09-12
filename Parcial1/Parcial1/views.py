from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1>Bienvenido, esta es la pagina inicial</h1>")
