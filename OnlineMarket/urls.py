from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from saved import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("user.urls")),
    path('auth/', include("djoser.urls")),
    path('auth/', include("djoser.urls.jwt")),
    path('', include("product.urls")),
    path('', include("event.urls")),
    path('', include("service.urls")),
    path('', include('saved.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)