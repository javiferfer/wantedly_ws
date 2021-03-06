from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^index/', views.index, name='index'),
	url(r'^register_user/$', views.register_user, name='register_user'),
	url(r'^login_user/$', views.login_user, name='login_user'),
	url(r'^logout_user/$', views.logout_user, name='logout_user'),
	url(r'^main_page/$', views.main_page, name='main_page'),
	url(r'^profile_page/$', views.profile_page, name='profile_page'),
	url(r'^users_page/$', views.users_page, name='users_page'),
]