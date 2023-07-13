
from django.contrib import admin
from django.urls import path, include
from main.views import index

from django.conf import settings
from django.conf.urls.static import static
from main import views  


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('news/', include('news.urls')),
    path('about', views.about, name='about'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

