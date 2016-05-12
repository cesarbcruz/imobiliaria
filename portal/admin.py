from django.contrib import admin
from .models import TipoImovel, Cidade, Bairro , Imovel, Destaque
from portal.models import Proprietario


class ImovelAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__', 'tipo', 'get_tipo_negociacao', 'proprietario']
    list_display_links = ['id', '__str__']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            readonly_fields = ('usuario',)
            return self.readonly_fields

        fields = [f.name for f in self.model._meta.fields]
        return fields




    def save_model(self, request, obj, form, change):
        if getattr(obj, 'usuario', None) is None:
            obj.usuario = request.user
        obj.save()

class DestaqueAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__', 'data_inicio_divulgacao', 'data_final_divulgacao']
    list_display_links = ['id', '__str__']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            readonly_fields = ('usuario',)
            return self.readonly_fields

        fields = [f.name for f in self.model._meta.fields]
        return fields

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'usuario', None) is None:
            obj.usuario = request.user
        obj.save()

class ProprietarioAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__', 'telefone_fixo', 'celular_1', 'email']
    list_display_links = ['id', '__str__']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            readonly_fields = ('usuario',)
            return self.readonly_fields

        fields = [f.name for f in self.model._meta.fields]
        return fields

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'usuario', None) is None:
            obj.usuario = request.user
        obj.save()

class TipoImovelAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.readonly_fields

        fields = [f.name for f in self.model._meta.fields]
        return fields

class CidadeAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.readonly_fields

        fields = [f.name for f in self.model._meta.fields]
        return fields

class BairroAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.readonly_fields

        fields = [f.name for f in self.model._meta.fields]
        return fields

admin.site.register(Proprietario, ProprietarioAdmin)
admin.site.register(TipoImovel, TipoImovelAdmin)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Bairro, BairroAdmin)
admin.site.register(Imovel, ImovelAdmin)
admin.site.register(Destaque, DestaqueAdmin)