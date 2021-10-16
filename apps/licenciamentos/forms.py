from django import forms
from apps.tipologias.models import Tipologia

class VerificaDocLicenciamentoForm(forms.ModelForm):
    class Meta:
        model = Tipologia
        fields = 'codigo', 'subgrupo', 'descricao', 'und_medida_desc', 'p_poluidor'
