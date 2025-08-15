from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mi_banco.urls')),  # Este incluye las URLs de tu app
]
