from django.contrib import admin
from apps.divisoes.models import Divisao


@admin.register(Divisao)
class DivisaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao')
    search_fields = ('codigo', 'descricao')
