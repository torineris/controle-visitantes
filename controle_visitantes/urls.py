from django.contrib import admin
from django.urls import path

from usuarios.views import index
from visitantes.views import registrar_visitante

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index",),
    path("registrar-visitante/", registrar_visitante, name="registrar_visitante",)
]
