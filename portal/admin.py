from django.contrib import admin
from .models import TipoImovel, Cidade, Bairro , Imovel

admin.site.register(TipoImovel)
admin.site.register(Cidade)
admin.site.register(Bairro)
admin.site.register(Imovel)