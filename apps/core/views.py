from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# @login_required(login_url='/contas/login/')
def index(request):
    template_name = 'index.html'
    return render(request, template_name)
