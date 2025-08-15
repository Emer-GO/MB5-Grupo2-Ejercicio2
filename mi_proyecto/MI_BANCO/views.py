from django.shortcuts import render

def inicio(request):
    contexto = {
        'nombre': 'Emer'
    }
    return render(request, 'MI_BANCO/inicio.html', contexto)