from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from apps.tipologias.models import Tipologia


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
