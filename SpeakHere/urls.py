
from django.contrib import admin
from django.urls import path ,include
from  django.conf import settings
from  django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SpeakHere_landing.urls')),
     path('app/', include('SpeakHere_app.urls')),
    path('auth/', include('SpeakHere_auth.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)