from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.admin import User
from apps.tipologias.models import Tipologia
from django.core.mail import send_mail
from .forms import TipologiaForm


def handler404(request, *args, **argv):
    response = render('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


@login_required(login_url='/contas/login/')
def listar_tipologias(request):
    template_name = 'tipologias/listar_tipologias.html'
    form = Tipologia.objects.all()
    context = {
        'form': form,
    }
    return render(request, template_name, context)


@login_required(login_url='/contas/login/')
def adicionar_tipologia(request):
    template_name = 'tipologias/adicionar_tipologia.html'
    context = {}
    if request.method == 'POST':
        form = TipologiaForm(request.POST, request.FILES)
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
    form = TipologiaForm(request.POST or None, request.FILES or None, instance=tipologia)
    if form.is_valid():
        form.save()
        return redirect('tipologias:listar_tipologias')
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='/contas/login')
def excluir_tipologia(request, id):
    template_name = 'tipologias/excluir_tipologia.html'
    form = Tipologia.objects.get(id=id)
    context = {'form': form}
    if request.method == 'POST':
        form.delete()
        return redirect('tipologias:listar_tipologias')
    return render(request, template_name, context)


def enviar_email_tipologia(request, id):
    tipologia = Tipologia.objects.get(id=1)
    assunto = 'Resumo da Tipologia'
    html_completo = render_to_string('tipologias/tipologia_email.html', {'tipologia', tipologia})
    corpo_email = 'Listagem das Tipologias'
    email_remetente = [User.email, ]
    email_destino = 'rbmdesenvolvimento@gmail.com'
    send_mail(assunto, corpo_email, email_remetente, email_destino, html_message=html_completo)

    return redirect('tipologias:enviar_tipologia_id')
