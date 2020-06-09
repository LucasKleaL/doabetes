from django.db import models
from django.conf import settings
from django.utils import timezone

class Anuncio(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    descricao = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    fotoProduto = models.ImageField(uploud_to='', blank=True, null=True, verbose_name='Foto do Produto')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
