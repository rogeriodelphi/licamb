from django.contrib import admin
from apps.licenciamentos.models import DocumentacaoLicenciamento


@admin.register(DocumentacaoLicenciamento)
class DocumentacaoLicenciamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'arquivo', 'status')
