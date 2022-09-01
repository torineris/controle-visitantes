from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    context = {
        "nome_pagina": "Início da dashboard",
    }
    return render(request, "index.html", context)

