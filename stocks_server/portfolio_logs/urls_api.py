from django.conf.urls import patterns, include, url

urlpatterns = patterns('portfolio_logs.views_api',
    url(r'^portfolio/(?P<portfolio_id>\d+)/$', 'portfolio'),
)