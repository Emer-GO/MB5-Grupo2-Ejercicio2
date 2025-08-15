from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login, get_user_model

User = get_user_model()

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
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Buscar el usuario por email en el modelo correcto
            usuario = User.objects.get(email=email)
            user = authenticate(request, username=usuario.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            return redirect('inicio')  # Asegúrate de tener esta URL en urls.py
        else:
            messages.error(request, 'Usuario o contraseña incorrecta')

    return render(request, 'mi_banco/login.html')
