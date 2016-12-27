from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class UserForm(forms.ModelForm):
	
	class Meta:
		model = User
		fields = ('username', 'password', 'email',)

class LoginForm(AuthenticationForm):
	
	username = forms.CharField(label="Nome Usuario", max_length=245)                               
	password = forms.CharField(label="Senha")