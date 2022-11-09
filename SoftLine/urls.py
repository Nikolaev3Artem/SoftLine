from django.conf.urls.i18n import i18n_patterns
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from main import views


urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', views.index),
    path('about/', views.about),
    path('error/', views.error),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
