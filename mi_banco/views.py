from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib import messages


#Inicio
def inicio(request):
    return render(request, 'mi_banco/inicio.html')



##  def registro(request):
##    return render(request, 'mi_banco/registro.html')


#Usuario Registro
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # O donde quieras redirigir
    else:
        form = RegistroForm()
    return render(request, 'mi_banco/registro.html', {'form': form})

#Usuario Login
def login_view(request):
    return render(request, 'mi_banco/login.html')
