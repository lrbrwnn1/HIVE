from django.conf.urls import url


from . import views

urlpatterns = [
	url(r'^LSI', views.LSI, name='LSI'),
	url(r'^profile', views.profile, name='profile'),
	url(r'^results', views.results, name='results'),
	url(r'', views.index, name='index'),


    
]
