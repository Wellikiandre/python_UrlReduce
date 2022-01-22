
# Create your views here.
from devwellik.projeto.encurtador.models import UrlRedirect
from django.shortcuts import redirect
from django.shortcuts import render

def redirecionar(requisicao, slug):
    parametroUrlRecuperada = UrlRedirect.objects.get(slug=slug)
    return redirect (parametroUrlRecuperada.destino)


