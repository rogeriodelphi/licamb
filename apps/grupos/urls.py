from django.urls import path
from . import views

app_name = 'apps.grupos'

urlpatterns = [
    path('listar_grupos/', views.listar_grupos, name = 'listar_grupos'),
]
