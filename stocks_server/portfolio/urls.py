from django.conf.urls import patterns, url, include

urlpatterns = patterns('portfolio.views',
    (r'^$', 'index'),
    (r'^(?P<portfolio_id>\d+)/$', 'portfolio'),
)