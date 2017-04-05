from __future__ import unicode_literals

from django.db import models

class Material(models.Model):
	nome_material = models.CharField(max_length=200, null=False)
	tipo_material = models.CharField(max_length=200, null=False)
	unidade_medida = models.CharField(max_length=200, null=False)	
	
	def __str__(self):
		return self.nome_material

class Estoque(models.Model):
	quantidade_material = models.IntegerField(null=False)
	materiais = models.ForeignKey(Material, on_delete=models.CASCADE)

	def __str__(self):
		return self.quantidade_material

class RecebimentoMaterial(models.Model):
	responsavel_pelo_recebimento = models.CharField(max_length=200)
	data_recebimento = models.DateTimeField(blank=True, null=False)


