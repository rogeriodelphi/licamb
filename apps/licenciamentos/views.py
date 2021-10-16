from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.licenciamentos.forms import VerificaDocLicenciamentoForm

# @login_required(login_url='/contas/login/')
def verifica_doc_licenciamento(request):
    template_name = 'licenciamentos/verifica_doc_licenciamento.html'
    form = VerificaDocLicenciamentoForm()
    context = {'form': form}
    return render(request, template_name, context)
