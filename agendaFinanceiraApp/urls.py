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
	url(r'^sair/$', views.sair, name='sair'),										
	url(r'^menu/$', views.menu, name='menu'),
	url(r'^consultar/receita/$', views.consultaReceita, name='consultaReceita'),
	url(r'^consultar/despesa/$', views.consultaDespesa, name='consultaDespesa'),
	url(r'^cadastrar/receita/$', views.casdatrarReceita, name='cadastrarReceita'),
	url(r'^cadastrar/despesa/$', views.casdatrarDespesas, name='cadastrarDespesa'),
	url(r'^editar/receita/(?P<id>[0-9]+)/$', views.editarReceita, name='editarReceita'),
	url(r'^editar/despesa/(?P<id>[0-9]+)/$', views.editarDespesa, name='editarDespesa'),
	url(r'^saldo/$', views.saldo, name='saldo'),
]