from django.urls import path
from . import views

app_name = 'apps.divisoes'

urlpatterns = [
    path('listar_grupos/', views.listar_grupos, name = 'listar_grupos'),
]
