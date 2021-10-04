from django.urls import path
from . views import (
    listar_tipologias,
    adicionar_tipologia,
    editar_tipologia,
    excluir_tipologia,
)

app_name = 'apps.tipologias'

urlpatterns = [
    path('listar_tipologias/', listar_tipologias, name = 'listar_tipologias'),
    path('adicionar_tipologia/', adicionar_tipologia, name='adicionar_tipologia'),
    path('editar_tipologia/<int:id>/', editar_tipologia, name='editar_tipologia'),
    path('excluir_tipologia/<int:id>', excluir_tipologia, name='excluir_tipologia'),
]
