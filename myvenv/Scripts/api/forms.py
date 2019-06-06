from .models import Talk
from django import forms
class productForm(forms.ModelForm):
	class Meta:
		model = Talk
		fields = '__all__'

