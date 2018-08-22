from django.conf.urls import url


from . import views

urlpatterns = [
	url(r'^LSI', views.LSI, name='LSI'),
	url(r'^profile', views.profile, name='profile'),
	url(r'^results', views.results, name='results'),
	url(r'', views.index, name='index'),
	#url(r'^profile/<str:username>', views.get_user_profile),
	#This is currently keeping the site from running, commenting it out for the moment so I can test some things. 
	#Feel free to reactivate when you need it! 

    
]
