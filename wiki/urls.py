from django.conf.urls.defaults import *

urlpatterns = (
    url(r'^view/(?P<id>\d+)/$', 'wiki.views.viewPost', name='viewPost'),
    url(r'^edit/(?P<id>\d+)/$', 'wiki.views.editPost', name='editPost'),
)
	
urlpatterns = patterns('', *urlpatterns)
