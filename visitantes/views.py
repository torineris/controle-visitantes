from django.shortcuts import render
from visitantes.forms import VisitanteForm

def registrar_visitante(request):

    form = VisitanteForm()

    if request.method =="POST":
        form = VisitanteForm(request.POST)

        if form.is_valid():
            form.save()

    context = {
        "nome_pagina": "Registrar visitante",
        "form": form
    }

    return render(request, "registrar_visitante.html", context)
