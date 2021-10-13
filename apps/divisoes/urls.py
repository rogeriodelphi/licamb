from django.urls import path
from . import views

app_name = 'apps.divisoes'

urlpatterns = [
    path('listar_divisoes/', views.listar_divisoes, name='listar_divisoes'),
    # path('adicionar_divisao/', views.adicionar_divisao, name = 'adicionar_divisao'),
    # path('editar_divisao/<int:id>/', views.editar_divisao, name = 'editar_divisao'),
    # path('excluir_divisao/<int:id>/', views.excluir_divisao, name = 'excluir_divisao'),
]
