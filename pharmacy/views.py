from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DetailView
from pharmacy.models import PharmacyModel
from pharmacy.forms import PharmacyForm

# Create your views here.
class PharmacyView(ListView):
	template_name='medicine.html'
	model=PharmacyModel
	context_object_name='pharmacy'

class AddMedicine(CreateView):
	template_name='addmedicine.html'
	form_class=PharmacyForm
	success_url='/pharmacy/medicine/'

#edit
class MedicineEditView(UpdateView):
	template_name='medicineedit.html'
	model=PharmacyModel
	fields=['medicine_name','quantity','mfd','expd','price']
	success_url='/pharmacy/medicine/'

#detail
class MedicineDetailView(DetailView):
	template_name='medicinedetail.html'
	model=PharmacyModel
