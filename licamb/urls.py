from apps.core import urls as core_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_urls)),
    path('contas/', include('apps.accounts.urls', namespace='accounts')),
    # path('', include('core.urls', namespace='core')),
    # path('', include('apps.divisoes.urls', namespace='divisoes')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "LICAMB - Sistema de Licenciamento"
admin.site.site_title = "LICAMB - Sistema de Licenciamento"
admin.site.index_title = "LICAMB - Sistema de Licenciamento"
