from django import forms
from master.models import UserRegisterModel,AddDepartmentModel,StaffRegistrationModel,AddAppoinmentModel,AddLeaveViewModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegisterForm(UserCreationForm):
	class Meta:
		model=User
		fields=["username","first_name","last_name","password1","password2","email"]

class ExtendedUserForm(forms.ModelForm):
	class Meta:
		model=UserRegisterModel
		fields=["age","address","id_card"]

class AddDepartmentForm(forms.ModelForm):
	class Meta:
		model=AddDepartmentModel
		exclude=('Created_on',)

class StaffUserRegisterForm(UserCreationForm):
	class Meta:
		model=User
		fields=["username","first_name","last_name","password1","password2","email","is_staff"]

class StaffRegistrationForm(forms.ModelForm):
	class Meta:
		model=StaffRegistrationModel
		fields=["age","address","profile"]

class AddAppoinmentForm(forms.ModelForm):
	class Meta:
		model=AddAppoinmentModel
		fields=["department","doctorname","appoinment_time","appoinment_date"]

class AddLeaveForm(forms.ModelForm):
	class Meta:
		model=AddLeaveViewModel
		fields=["department","name","leave_type","Start_date","end_date"]
		

class Subscribe(forms.Form):
	Email = forms.EmailField()
	def __str__(self):
		return self.Email
