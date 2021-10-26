from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.tipologias.models import Tipologia

# @login_required(login_url='/contas/login/')
def verifica_doc_licenciamento(request):
    template_name = 'licenciamentos/verifica_doc_licenciamento.html'
    tipologias = Tipologia.objects.all()
    context = {
        'tipologias': tipologias,
    }
    return render(request, template_name, context)
