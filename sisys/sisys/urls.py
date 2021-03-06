from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sisys.home_app.urls')),
    path('accounts/', include('sisys.sisis_auth.urls')),
    path('blog/', include('sisys.blog_app.urls')),
    path('shopping/', include('sisys.shopping_app.urls')),
    path('newsletters/', include('sisys.newsletters_app.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
