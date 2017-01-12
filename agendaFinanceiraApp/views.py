import datetime 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ReceitaForm, DespesaForm
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

# Logout
def sair(request):
	logout(request)
	return redirect('/')

# -----views com obrigatoriedade de login-----
	
# Menu inical apos login
@login_required
def menu(request):
	return render(request, 'agendaFinanceiraApp/menu.html', {})


# Busca receitas
@login_required
def consultaReceita(request):
	receitas = []
	
	if (request.GET.get('data_inicio') is not None) & (request.GET.get('data_fim') is not None):
		data_inicio = request.GET.get('data_inicio')
		data_fim = request.GET.get('data_fim')
		
		# conversao e formatacao da data 
		data_inicio = datetime.datetime.strptime(data_inicio, "%d/%m/%Y").strftime("%Y-%m-%d %H:%M:%S")
		data_fim = datetime.datetime.strptime(data_fim, "%d/%m/%Y").strftime("%Y-%m-%d %H:%M:%S")	
		receitas = Receita.objects.filter(usuario=request.user, data_entrada__range=(data_inicio, data_fim)).order_by('data_entrada')
	
	return render(request, 'agendaFinanceiraApp/consultaReceita.html', {'receitas': receitas})

# Busca despesas
@login_required
def consultaDespesa(request):
	despesas = []

	if (request.GET.get('data_inicio') is not None) & (request.GET.get('data_fim') is not None):
		data_inicio = request.GET.get('data_inicio')
		data_fim = request.GET.get('data_fim')
		
		# conversao e formatacao da data 
		data_inicio = datetime.datetime.strptime(data_inicio, "%d/%m/%Y").strftime("%Y-%m-%d %H:%M:%S")
		data_fim = datetime.datetime.strptime(data_fim, "%d/%m/%Y").strftime("%Y-%m-%d %H:%M:%S")	
		despesas = Despesas.objects.filter(usuario=request.user, data_vencimento__range=(data_inicio, data_fim)).order_by('data_vencimento')
	
	return render(request, 'agendaFinanceiraApp/consultaDespesa.html', {'despesas': despesas})

# Cadastro de receita
@login_required
def casdatrarReceita(request):
	if request.method == "POST":
		receitaForm = ReceitaForm(request.POST)
		if receitaForm.is_valid():
			receita = receitaForm.save(commit=False)
			receita.usuario = request.user
			receita.save()
			return redirect('/consultar/receita/')
	else:
		receitaForm = ReceitaForm()
		return render(request, 'agendaFinanceiraApp/cadastroReceita.html', {'form': receitaForm})

# Cadastro de despesas
@login_required
def casdatrarDespesas(request):
	if request.method == "POST":
		despesaForm = DespesaForm(request.POST)
		if despesaForm.is_valid():
			despesa = despesaForm.save(commit=False)
			despesa.usuario = request.user
			despesa.save()
			return redirect('/consultar/despesa/')
	else:
		despesaForm = DespesaForm()
		return render(request, 'agendaFinanceiraApp/cadastroDespesa.html', {'form': despesaForm})

# Editar Receita
@login_required
def editarReceita(request, id):
	receita = Receita.objects.get(pk=id)
	if request.method == "POST":
		receitaEditForm = ReceitaForm(request.POST, instance=receita)
		if receitaEditForm.is_valid():
			receita = receitaEditForm.save(commit=False)
			receita.save()
			return redirect('/consultar/receita/')
	else:
		receitaEditForm = ReceitaForm(instance=receita)
		return render(request, 'agendaFinanceiraApp/cadastroReceita.html', {'form': receitaEditForm})


@login_required
def editarDespesa(request, id):
	despesa = Despesas.objects.get(pk=id)
	if request.method == "POST":
		despesaEditForm = DespesaForm(request.POST, instance=despesa)
		if despesaEditForm.is_valid():
			despesa = despesaEditForm.save(commit=False)
			despesa.save()
			return redirect('/consultar/despesa/')
	else:
		despesaEditForm = DespesaForm(instance=despesa)
		return render(request, 'agendaFinanceiraApp/cadastroDespesa.html', {'form': despesaEditForm})
