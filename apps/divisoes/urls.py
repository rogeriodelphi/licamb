from django.urls import path
from . import views

app_name = 'apps.divisoes'

urlpatterns = [
    path('listar_divisoes/', views.listar_divisoes, name = 'listar_divisoes'),
]
