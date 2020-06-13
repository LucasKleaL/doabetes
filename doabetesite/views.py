from django.shortcuts import render

def home(request):
    return render(request, 'site/home.html', {})
def registro(request):
    return render(request, 'site/paginaRegistro.html', {})
def login(request):
    return render(request, 'registration/login.html', {})
def sobre(request):
    return render(request, 'site/paginaSobre.html', {})
def contato(request):
    return render(request, 'site/paginaContato.html', {})
def produtos(request):
    return render(request, 'site/paginaProdutos.html', {})

