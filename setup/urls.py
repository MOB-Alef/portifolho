from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/projetos/', permanent=False)),  # Redireciona a raiz para /projetos/
    path('admin/', admin.site.urls),
    path('projetos/', include('projetos.urls')),
    path('blog/', include('blog.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)