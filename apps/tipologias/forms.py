from django import forms
from .models import Tipologia


class TipologiaForm(forms.ModelForm):
    class Meta:
        model = Tipologia
        fields = ('codigo', 'descricao', 'subgrupo', 'und_medida_desc', 'p_poluidor')
