from django.contrib import admin
from apps.tipologias.models import Tipologia, Unidade_Medida

@admin.register(Tipologia)
class TipologiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'subgrupo', 'descricao')
    search_fields = ('codigo', 'subgrupo', 'divisao')

@admin.register(Unidade_Medida)
class UnidadeMedidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'und_medida_desc')
    search_fields = ('und_medida_desc',)