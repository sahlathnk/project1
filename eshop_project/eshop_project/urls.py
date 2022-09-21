from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from eshop_project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shopapp/',include('eshop_app.urls')),
    path('searchapp/',include('eshop_Searchapp.urls')),
    path('cartapp/',include('eshop_cartapp.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
