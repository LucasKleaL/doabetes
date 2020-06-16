from django.contrib import admin

from .models import Marca
from .models import Produto
from .models import MarcaProduto


admin.site.register(MarcaProduto)

admin.site.register(Produto)

admin.site.register(Marca)