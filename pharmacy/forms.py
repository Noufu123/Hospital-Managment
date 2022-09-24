from django import forms
from pharmacy.models import PharmacyModel 

class PharmacyForm(forms.ModelForm):
	class Meta:
		model=PharmacyModel
		exclude=('Created_on',)
