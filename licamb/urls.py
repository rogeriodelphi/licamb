from apps.core import urls as core_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_urls)),
    path('contas/', include('apps.accounts.urls', namespace='accounts')),
    path('divisoes/', include('apps.divisoes.urls', namespace='divisoes')),
    path('grupos/', include('apps.grupos.urls', namespace='grupos')),
    path('subgrupos/', include('apps.subgrupos.urls', namespace='subgrupos')),
    path('tipologias/', include('apps.tipologias.urls', namespace='tipologias')),
    path('licenciamentos/', include('apps.licenciamentos.urls', namespace='licenciamentos')),
]
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "LICAMB - Sistema de Licenciamento"
admin.site.site_title = "LICAMB - Sistema de Licenciamento"
admin.site.index_title = "LICAMB - Sistema de Licenciamento"
