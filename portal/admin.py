from django.contrib import admin
from .models import TipoImovel, Cidade, Bairro , Imovel, Destaque
from portal.models import Proprietario


class ImovelAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__', 'tipo', 'get_tipo_negociacao', 'proprietario']
    list_display_links = ['id', '__str__']
    readonly_fields=('usuario',)


    def save_model(self, request, obj, form, change):
        if getattr(obj, 'usuario', None) is None:
            obj.usuario = request.user
        obj.save()

class DestaqueAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__', 'data_inicio_divulgacao', 'data_final_divulgacao']
    list_display_links = ['id', '__str__']
    readonly_fields=('usuario',)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'usuario', None) is None:
            obj.usuario = request.user
        obj.save()

class ProprietarioAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__', 'telefone_fixo', 'celular_1', 'email']
    list_display_links = ['id', '__str__']
    readonly_fields=('usuario',)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'usuario', None) is None:
            obj.usuario = request.user
        obj.save()

admin.site.register(Proprietario, ProprietarioAdmin)
admin.site.register(TipoImovel)
admin.site.register(Cidade)
admin.site.register(Bairro)
admin.site.register(Imovel, ImovelAdmin)
admin.site.register(Destaque, DestaqueAdmin)