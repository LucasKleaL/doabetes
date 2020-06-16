from django.shortcuts import render
from .models import Produto
from .models import MarcaProduto

from django.shortcuts import get_list_or_404

def home(request):
    return render(request, 'site/home.html', {})
def registro(request):
    return render(request, 'registration/registro.html', {})
def login(request):
    return render(request, 'registration/login.html', {})
def sobre(request):
    return render(request, 'site/paginaSobre.html', {})
def contato(request):
    return render(request, 'site/paginaContato.html', {})
def produtos(request):
    marcaProdutos = get_list_or_404(MarcaProduto)
    return render(request, 'site/paginaProdutos.html', {'marcaProdutos': marcaProdutos})

def depoimentos(request):
    return render(request, 'site/paginaDepoimentos.html', {})

