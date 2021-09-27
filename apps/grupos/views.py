from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from apps.grupos.models import Grupo


def handler404(request, *args, **argv):
    response = render('404.html', {},
                      context_instance=RequestContext(request))
    response.status_code = 404
    return response

# DIVISÃO
# @login_required(login_url='/cadastros/vacinas/login/')
def listar_grupos(request):
    template_name = 'grupos/listar_grupos.html'
    form = Grupo.objects.all()
    context = {'form': form}
    return render(request, template_name, context)
