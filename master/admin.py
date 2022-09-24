from django.contrib import admin
from master.models import UserRegisterModel,AddDepartmentModel,StaffRegistrationModel,AddAppoinmentModel,AddLeaveViewModel

# Register your models here.
admin.site.register(UserRegisterModel)
admin.site.register(AddDepartmentModel)
admin.site.register(StaffRegistrationModel)
admin.site.register(AddAppoinmentModel)
admin.site.register(AddLeaveViewModel)
