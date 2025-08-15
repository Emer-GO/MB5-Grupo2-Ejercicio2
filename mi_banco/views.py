from django.shortcuts import render

def inicio(request):
    return render(request, 'mi_banco/inicio.html')

def registro(request):
    return render(request, 'mi_banco/registro.html')

def login_view(request):
    return render(request, 'mi_banco/login.html')
