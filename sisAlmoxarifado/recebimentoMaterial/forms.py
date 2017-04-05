from django import forms
from .models import Material

class cadastro_material(forms.ModelForm):
	class Meta:
		model = Material
		fields = ('Nome', 'Tipo', 'Unidade')