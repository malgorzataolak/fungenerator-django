from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.conf.urls import url, include
from . import views


urlpatterns=[ url(r'^$', views.main_page, name='main_page'),
	url(r'^tickle/', views.tickle, name='tickle'),
	url(r'^tickle_start/', views.tickle_start, name='tickle_start'),
	url(r'^tickle_fast/', views.tickle_fast, name='tickle_fast'),
	url(r'^tickle_normal/', views.tickle_normal, name='tickle_normal'),
	url(r'^tickle_slow/', views.tickle_slow, name='tickle_slow'),
	url(r'^funny_movies/', views.funny_movies, name='funny_movies'),
	url(r'^funny_pictures/', views.funny_pictures, name='funny_pictures'),
	url(r'^jokes/', views.jokes, name='jokes'),
	url(r'^bubblewrap/', views.bubblewrap, name='bubblewrap'),
	url(r'^settings/', views.settings, name='settings'),
	url(r'^change_password/', views.change_password, name='change_password'),
]
