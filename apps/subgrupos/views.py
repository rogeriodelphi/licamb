from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from apps.subgrupos.models import SubGrupo


def handler404(request, *args, **argv):
    response = render('404.html', {},
                      context_instance=RequestContext(request))
    response.status_code = 404
    return response

# DIVISÃO
# @login_required(login_url='/cadastros/vacinas/login/')
def listar_subgrupos(request):
    template_name = 'subgrupos/listar_subgrupos.html'
    form = SubGrupo.objects.all()
    context = {'form': form}
    return render(request, template_name, context)
