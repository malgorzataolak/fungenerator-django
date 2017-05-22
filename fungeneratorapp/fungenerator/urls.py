from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.conf.urls import url, include
from . import views


urlpatterns=[ url(r'^$', views.main_page, name='main_page'),
	url(r'^tickle/', views.tickle, name='tickle'),
	url(r'^funny_movies/', views.funny_movies, name='funny_movies'),
	url(r'^funny_pictures/', views.funny_pictures, name='funny_pictures'),
	url(r'^jokes/', views.jokes, name='jokes'),
	url(r'^bubblewrap/', views.bubblewrap, name='bubblewrap'),
	url(r'^settings/', views.settings, name='settings'),


]