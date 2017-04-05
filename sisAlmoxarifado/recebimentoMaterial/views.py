from django.shortcuts import render
from .models import Material

def novo_material(request):

	form = postForm()
	return render(request, 'recebimentoMaterial/novo_material.html', {'form':form})

def home_page(request):
	return render(request, 'recebimentoMaterial/home_page.html', {})