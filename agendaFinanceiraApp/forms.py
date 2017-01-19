from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Receita, Despesas
from django.utils.translation import ugettext_lazy as _

class UserForm(forms.ModelForm):
	password = forms.CharField(max_length=30, widget=forms.PasswordInput) 

	class Meta:
		model = User
		fields = ('username', 'password', 'email',)
		labels = {'username': _('Usuario'), 
					'password': _('Senha'),}
		#widget = { 'password': forms.PasswordInput(), } # NAO ESTA DANDO CERTO!!! 

class LoginForm(AuthenticationForm):
	username = forms.CharField(label="Nome Usuario", max_length=150)                               
	password = forms.CharField(label="Senha", widget=forms.PasswordInput)

class ReceitaForm(forms.ModelForm):
	valor = forms.CharField(max_length=12)

	class Meta:
		model = Receita
		fields = ('nome_pagador', 'valor', 'data_entrada', 'forma_recebimento', 'situacao', 'observacoes')
		widget = {'observacoes': forms.Textarea(attrs={'cols': 80, 'rows': 10}),}

class DespesaForm(forms.ModelForm):
	valor = forms.CharField(max_length=12)

	class Meta:
		model = Despesas
		fields = ('nome_credor', 'valor', 'data_vencimento', 'forma_recebimento', 'situacao', 'observacoes')
		labels = {'forma_recebimento': _('Forma de Pagamento'),}
		widget = {'observacoes': forms.Textarea(attrs={'cols': 80, 'rows': 10}),}