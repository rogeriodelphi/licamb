from django.contrib import admin
from apps.grupos.models import Grupo

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'divisao', 'descricao')
    search_fields = ('codigo', 'divisao')