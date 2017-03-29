from __future__ import unicode_literals

from django.db import models

class Material(models.Model):
	nome_material = models.CharField(max_length=200)
	tipo_material = models.CharField(max_length=200)
	unidade_medida = models.CharField(max_length=200)	
	
	def __str__(self):
		return self.nome_material

class SetorRequisitante(models.Model):
	nome_setorRequisitante = models.CharField(max_length=200)

	def __str__(self):
		return self.nome_setorRequisitante

class Estoque(models.Model):
	quantidade_material = models.IntegerField()
	materiais = models.ForeignKey(Material, on_delete=models.CASCADE)

	def __str__(self):
		return self.quantidade_material

class RecebimentoMaterial(models.Model):
	responsavel_pelo_recebimento = models.CharField(max_length=200)
	data_recebimento = models.DateTimeFields(blank=True, null=True)


