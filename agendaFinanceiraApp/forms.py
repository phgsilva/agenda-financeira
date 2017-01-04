from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Receita, Despesas


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password', 'email',)
		labels = {'username': _('Usuario'), 
					'password': _('Senha'),}
		widget = { 'password': forms.PasswordInput(), }

class LoginForm(AuthenticationForm):
	username = forms.CharField(label="Nome Usuario", max_length=245)                               
	password = forms.CharField(label="Senha", widget=forms.PasswordInput)

class ReceitaForm(forms.ModelForm):
	class Meta:
		model = Receita
		fields = ('nome_pagador', 'valor', 'data_entrada', 'forma_recebimento', 'situacao', 'observacoes')

class DespesaForm(forms.ModelForm):
	class Meta:
		model = Despesas
		fields = ('nome_credor', 'valor', 'data_vencimento', 'forma_recebimento', 'situacao', 'observacoes')