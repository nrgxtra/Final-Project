from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_app.urls')),
    path('accounts/', include('sisis_auth.urls')),
    path('blog/', include('blog_app.urls')),
    path('shopping/', include('shopping_app.urls')),
    path('newsletters/', include('newsletters_app.urls')),
    path('common/', include('common.urls')),
]
handler404 = "common.views.page_not_found_view"

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
