from django.urls import path
from . import views

app_name = 'apps.tipologias'

urlpatterns = [
    path('listar_tipologias/', views.listar_tipologias, name = 'listar_tipologias'),
    path('adicionar_tipologia/', views.adicionar_tipologia, name='adicionar_tipologia'),
]
