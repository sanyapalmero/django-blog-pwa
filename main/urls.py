from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/blog/', include('blog.admin_urls')),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', include('blog.urls')),
    path('', include('pwa.urls'))
]


if settings.DEBUG:
    urlpatterns = static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    ) + urlpatterns
