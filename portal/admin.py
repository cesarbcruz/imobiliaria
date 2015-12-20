from django.contrib import admin
from .models import TipoImovel, Cidade, Bairro , Imovel


class ImovelAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__']
    list_display_links = ['id', '__str__']

admin.site.register(TipoImovel)
admin.site.register(Cidade)
admin.site.register(Bairro)
admin.site.register(Imovel, ImovelAdmin)