from django.db import models
from django.conf import settings
from django.utils import timezone

class Anuncio(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    descricao = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Marca(models.Model):
    nome = models.CharField(max_length=200, default="")

class Produto(models.Model):
    nome = models.CharField(max_length=200, default=" ", unique=True)
    nomeImagem = models.CharField(max_length=200, default="")

class MarcaProduto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

