from django import forms
from apps.tipologias.models import Tipologia

# class VerificaDocLicenciamentoForm(forms.ModelForm):
#     class Meta:
#         model = Tipologia
#         fields = 'codigo', 'subgrupo', 'descricao', 'und_medida_desc', 'p_poluidor'



class VerificaDocLicenciamentoForm(forms.Form):
    tipologia = forms.CharField(label='Tipologia', max_length=100)
    und_medida_desc = forms.CharField(label='Unidade de Medida', max_length=100)
    p_poluidor = forms.DateField(label='Porte Poluidor')
    valor = forms.DateField(label='Porte Poluidor')
