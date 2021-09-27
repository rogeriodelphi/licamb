from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from apps.divisoes.models import Divisao


def handler404(request, *args, **argv):
    response = render('404.html', {},
                      context_instance=RequestContext(request))
    response.status_code = 404
    return response

# DIVISÃO
# @login_required(login_url='/cadastros/vacinas/login/')
def listar_divisoes(request):
    template_name = 'divisoes/listar_divisoes.html'
    form = Divisao.objects.all()
    context = {'form': form}
    return render(request, template_name, context)

