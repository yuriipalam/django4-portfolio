from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from portfolio.views import introduction_admin

handler404 = 'portfolio.views.handler404'

urlpatterns = [
    path('', include('portfolio.urls')),
    path('admin/portfolio/introduction/', view=introduction_admin),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
