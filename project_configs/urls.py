from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from project_configs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main_app.urls")),
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler400 = views.error_400
handler404 = views.error_404
handler500 = views.error_500