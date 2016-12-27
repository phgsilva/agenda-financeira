from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Receita(models.Model):
	SITUACOES = (('AB', 'Aberto'),
				('PG', 'Pagamento'))

	usuario = models.ForeignKey('auth.User')
	valor = models.FloatField()
	data_entrada = models.DateTimeField()
	nome_pagador = models.CharField(max_length=50)
	forma_recebimento = models.CharField(max_length=45)
	situacao = models.CharField(max_length=2, choices=SITUACOES)
	observacoes = models.TextField()

	def salvar(self):
		self.save()

class Despesas(models.Model):
	SITUACOES = (('AB', 'Aberto'),
				('PG', 'Pagamento'))		

	usuario = models.ForeignKey('auth.User')
	valor = models.FloatField()
	data_vencimento = models.DateTimeField()
	nome_credor = models.CharField(max_length=50)
	forma_recebimento = models.CharField(max_length=45)
	situacao = models.CharField(max_length=2, choices=SITUACOES)
	observacoes = models.TextField()

	def salvar(self):
		self.save()
	


		
