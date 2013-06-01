from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)

urlpatterns += (
    url(r'api/', include('app.urls')),
    url(r'', include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
