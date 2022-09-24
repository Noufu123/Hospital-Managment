from django.db import models

# Create your models here.
class PharmacyModel(models.Model):
	
	medicine_name=models.CharField(max_length=50)
	quantity=models.IntegerField()
	mfd=models.DateField()
	expd=models.DateField()
	price=models.IntegerField()
	Created_on=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.medicine_name

