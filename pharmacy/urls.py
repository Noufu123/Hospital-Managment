from django.urls import path,re_path
from pharmacy.views import PharmacyView,AddMedicine,MedicineEditView,MedicineDetailView

urlpatterns = [
	path('medicine/',PharmacyView.as_view(),name='medicine'),
	path('addmedicine/',AddMedicine.as_view(),name='addmedicine'),
	re_path(r'^edit/(?P<pk>\d+)$',MedicineEditView.as_view(),name='edit'),
	re_path(r'^detail/(?P<pk>\d+)$',MedicineDetailView.as_view(),name='medicinedetail')
]