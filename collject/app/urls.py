from django.conf.urls import patterns, url, include


urlpatterns = patterns('app.views',
    url(r'^$', 'index', name='index'),
)

