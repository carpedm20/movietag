from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studyplan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^follow/$', 'account.views.follow', name='follow'),

    url(r'^profile/$', 'account.views.view_profile', name='view_profile'),
    url(r'^sign_in/$', 'account.views.sign_in', name='sign_in'),
    url(r'^sign_up/$', 'account.views.sign_up', name='sign_up'),
    url(r'^sign_out/$', 'account.views.sign_out', name='sign_out'),
)
