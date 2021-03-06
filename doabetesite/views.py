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
def doacao(request):
    return render(request, 'site/doacao.html', {})
def doacaoEnviada(request):
    return render(request, 'site/doacaoEnviada.html', {})
def solicitacao(request):
    return render(request, 'site/solicitacao.html', {})
def solicitacaoEnviada(request):
    return render(request, 'site/solicitacaoEnviada.html', {})
def avisar(request):
    return
