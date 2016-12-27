from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm 


urlpatterns = [
	url(r'^$', views.index),
	url(r'^cadastrar/$', views.cadastrar, name='cadastrar'),
	url(r'^login/$', auth_views.login, {'template_name': 'agendaFinanceiraApp/login.html', 
										'redirect_field_name': '/menu.html',
										'authentication_form': LoginForm,}, 
										name='login',),
	url(r'^menu/$', views.menu, name='menu')
]