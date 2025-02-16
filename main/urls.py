
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
import portfolio.urls
urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('',include(portfolio.urls))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)