from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
appoinment_time_choice=(('10:00am to 11:00am','10:00am to 11:00am'),
						('11:00am to 12:00pm','11:00am to 12:00pm'))

leave_type_choice=(('personalleave','personalleave'),
				   ('medicalleave','medicalleave'),
				   ('emergencyleave','emergencyleave'))

approvel_status_choice=(('approve','approve'),
						('pending','pending'),
						('reject','reject'))


class UserRegisterModel(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	age=models.IntegerField(default=18)
	address=models.TextField(max_length=80)
	id_card=models.ImageField(upload_to="idcard/")
	status=models.BooleanField(default=True)
	created_on=models.DateTimeField(auto_now=True)
	def __str__(self):
		return (self.user.first_name+" "+self.user.last_name)

class AddDepartmentModel(models.Model):
	dept_id=models.CharField(max_length=50)
	dept_name=models.CharField(max_length=80)
	fees=models.IntegerField(default=200)
	def __str__(self):
		return self.dept_name


class StaffRegistrationModel(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	age=models.IntegerField()
	address=models.TextField()
	profile=models.ImageField(upload_to="idcard/")
	status=models.BooleanField(default=True)
	created_on=models.DateTimeField(auto_now=True)
	def __str__(self):
		return (self.user.first_name+" "+self.user.last_name)

class AddAppoinmentModel(models.Model):
	user=models.CharField(max_length=80)
	department=models.ForeignKey(AddDepartmentModel,on_delete=models.CASCADE)
	doctorname=models.ForeignKey(StaffRegistrationModel,on_delete=models.CASCADE)
	appoinment_time=models.CharField(max_length=50,choices=appoinment_time_choice)
	appoinment_date =models.DateField(null=False,help_text="Please provide thedate in YY/MM/DD")
	payment_status=models.BooleanField(default=False)
	status=models.BooleanField(default=True)
	created_on=models.DateTimeField(auto_now=True)
	def __str__(self):
		return (self.user)

class AddLeaveViewModel(models.Model):
	user=models.CharField(max_length=80)
	department=models.ForeignKey(AddDepartmentModel,on_delete=models.CASCADE)
	name=models.CharField(max_length=80)
	leave_type=models.CharField(max_length=50,choices=leave_type_choice)
	Start_date=models.DateField(null=False,help_text="Please provide thedate in YY/MM/DD")
	end_date=models.DateField(null=False,help_text="Please provide thedate in YY/MM/DD")
	approvel_status=models.CharField(max_length=50,choices=approvel_status_choice)
	status=models.BooleanField(default=True)
	created_on=models.DateTimeField(auto_now=True)
	def __str__(self):
		return(self.user)
