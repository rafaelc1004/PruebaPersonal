from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'personal/index.html')

def formulario(request):
    return render(request, 'personal/form_personal.html')

def listado(request):
    return render(request, "personal/list_personal.html")