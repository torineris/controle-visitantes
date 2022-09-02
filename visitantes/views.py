import re
from django.shortcuts import render

def registrar_visitante(request):

    context = {}

    return render(request, "registrar_visitante.html", context)
