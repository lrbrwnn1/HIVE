from django.conf.urls import include, url
#from django.urls import include, path

from . import views

urlpatterns = [
	url(r'^LSI', views.LSI, name='LSI'),
	url(r'^userprofile', views.userprofile, name='userprofile'),
	url(r'^results', views.results, name='results'),
	url(r'', views.index, name='index'), 
]

