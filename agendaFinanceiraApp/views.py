from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from .models import Receita, Despesas

# Create your views here.

# Pagina inicial
def index(request):
	return render(request, 'agendaFinanceiraApp/index.html', {})

# Cadastrar Usuario
def cadastrar(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user_salvo = User.objects.create_user(user.username, user.email, user.password)
			return redirect('/login/')
	else:
		form = UserForm()
	return render(request, 'agendaFinanceiraApp/cadastro.html', {'form': form})

# -----views com obrigatoriedade de login-----
	
# Menu inical apos login
@login_required
def menu(request):
	#if not request.user.is_authenticated():
	#	return redirect('login.html')
	#else:
		return render(request, 'agendaFinanceiraApp/menu.html', {})


# Busca receitas
@login_required
def consultaReceita(request):
	receitas = Receita.objects.order_by('data_entrada')
	return render(request, 'agendaFinanceiraApp/consultarReceitas.html', {'receitas': receitas})

# Busca despesas
@login_required
def consultaDespesa(request):
	despesas = Despesas.objects.order_by('data_vencimento')
	return render(request, 'agendaFinanceiraApp/ConsultarDespesas.html', {'despesas': despesas})


# Criar as views de caadastro despesa e cadastro receita!!



# Reaiza login de usuario *utilizando agora o do Django
'''def login(request):
	if(request.method == "POST"):
		usuario = request.POST['nome_usuario']
		senha = request.POST['senha']
		usuario = authenticate(username = username, password = password)
		if user is not None:
			login(request, usuario)
			return redirect('agendaFinanceiraApp.views.menu_inicial')
		else:
			return render('/erro')
	else:
		return render(request, 'agendaFinanceiraApp/login.html') '''





