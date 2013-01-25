from django.conf.urls import patterns, url

from downloader import views

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),
	url(r'^new_download/$', views.new_download, name = 'new_download'),
	url(r'^new_download/submit$', views.submit_new_download, name = 'submit_new_download'),
	url(r'^downloads_list/$', views.downloads_list, name = 'downloads_list'),
)

