from django.urls import path
from .views import verifica_doc_licenciamento


app_name = 'apps.licenciamentos'

urlpatterns = [
    path('verifica_doc_licenciamento/', verifica_doc_licenciamento, name='verifica_doc_licenciamento'),

]
