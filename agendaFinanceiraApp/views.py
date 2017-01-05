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
    return render(request, 'agendaFinanceiraApp/menu.html', {})


# Busca receitas
@login_required
def consultaReceita(request):
	data_inicio = request.GET.get('data_inicio')
	data_fim = request.GET.get('data_fim')
	receitas = []
	
	if (data_inicio is not None) and (data_fim is not None):
		receitas = Receita.objects.filter(user=request.user, data_entrada__range=(data_inicio, data_fim)).order_by('data_entrada')
	
	return render(request, 'agendaFinanceiraApp/consultarReceitas.html', {'receitas': receitas})

# Busca despesas
@login_required
def consultaDespesa(request):
	data_inicio = request.GET.get('data_inicio')
	data_fim = request.GET.get('data_fim')
	despesas = []

	if (data_inicio is not None) and (data_fim is not None):
		despesas = Despesas.objects.filter(user=request.user, data_vencimento__range=(data_inicio, data_fim)).order_by('data_vencimento')
	
	return render(request, 'agendaFinanceiraApp/ConsultarDespesas.html', {'despesas': despesas})


# Criar as views de caadastro despesa e cadastro receita!!
@login_required
def casdatrarReceita(request):
    pass

@login_required
def casdatrarDespesas(request):
    pass


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