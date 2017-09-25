
from django.conf.urls import url, include 
from . import views
from django.contrib.auth import views as auth_views



urlpatterns =[
url(r'^$', auth_views.login, {'template_name': 'homepage/login.html'}, name='login'),
url(r'^home/$', views.profile, name = 'home'),
url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
url(r'^signup/$', views.signup, name='signup'),
]