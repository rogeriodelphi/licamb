from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from apps.tipologias.models import Tipologia
from .forms import TipologiaForm


def handler404(request, *args, **argv):
    response = render('404.html', {},
                      context_instance=RequestContext(request))
    response.status_code = 404
    return response

# TIPOLOGIA
@login_required(login_url='/contas/login/')
def listar_tipologias(request):
    template_name = 'tipologias/listar_tipologias.html'
    form = Tipologia.objects.all()
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='/contas/login/')
def adicionar_tipologia(request):
    template_name = 'tipologias/adicionar_tipologia.html'
    context = {}
    if request.method == 'POST':
        form = TipologiaForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Categoria salva com sucesso.')
            return redirect('tipologias:listar_tipologias')
    # Se o método for get, renderiza o formulário em branco
    form = TipologiaForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login')
def editar_tipologia(request, id):
    template_name = 'tipologias/editar_tipologia.html'
    tipologia = Tipologia.objects.get(id=id)
    form = TipologiaForm(request.POST or None, instance=tipologia)
    if form.is_valid():
        form.save()
        return redirect('tipologias:listar_tipologias')
    context = {'form': form}
    return render(request, template_name, context)