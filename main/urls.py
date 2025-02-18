
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



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)