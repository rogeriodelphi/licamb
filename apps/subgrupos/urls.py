from django.urls import path
from . import views

app_name = 'apps.subgrupos'

urlpatterns = [
    path('listar_subgrupos/', views.listar_subgrupos, name='listar_subgrupos'),
]
