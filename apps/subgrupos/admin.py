from django.contrib import admin
from apps.subgrupos.models import SubGrupo


@admin.register(SubGrupo)
class SubGrupoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'grupo', 'descricao')
    search_fields = ('codigo', 'grupo', 'divisao')
