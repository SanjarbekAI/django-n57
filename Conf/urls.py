from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from common.views import home_page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page_view)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
