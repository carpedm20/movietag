from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from movie import views as m_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movietag.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'movie.views.index', name='index'),

    url(r'^m/', include('movie.urls', namespace='movie')),

    url(r'^admin/', include(admin.site.urls)),
)
