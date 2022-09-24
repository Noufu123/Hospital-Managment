
from django.shortcuts import render,redirect
# from django.views.generic import TemplateView,CreateView,ListView,View,UpdateView,DetailView
# from master.forms import StaffUserRegisterForm,UserRegisterForm,ExtendedUserForm,AddDepartmentForm,StaffRegistrationForm
from django.views.generic import*
from master.forms import*
from django.contrib.auth import authenticate,login,logout
from master.models import StaffRegistrationModel,UserRegisterModel,AddDepartmentModel,AddAppoinmentModel,AddLeaveViewModel
from django.contrib.auth.forms import AuthenticationForm
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest


from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm

from django.shortcuts import render
from hospital.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail




# Create your views here.
class HomeView(TemplateView):
	template_name='home.html'

class ProjectView(TemplateView):
	template_name='hshome3.html'

class LoginView(TemplateView):
	template_name='hslogin.html'


class ForgottenView(TemplateView):
	template_name='hsforgotten.html'

class ContactView(TemplateView):
	template_name='hscontact.html'

class AboutView(TemplateView):
	template_name='hsabout.html'

class IndexView(TemplateView):
	template_name='adhhome.html'

class StaffHomeView(TemplateView):
	template_name='staffhome.html'	

def adduser(request):
	if request.method=="POST":
		form=UserRegisterForm(request.POST)
		extend_form=ExtendedUserForm(request.POST,request.FILES)

		if form.is_valid() and extend_form.is_valid():
			user=form.save()
			extended_profile=extend_form.save(commit=False)
			extended_profile.user=user
			extended_profile.save()

			sub = forms.UserRegisterForm(request.POST)
			fname=str(sub['first_name'].value())
			lname=str(sub['last_name'].value())
			subject = 'Welcome to AM Hospital'
			message = 'Hi %s %s Hope you are enjoying your Day'%(fname,lname)
			recepient = str(sub['email'].value())
			send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently =False)

			username_var=form.cleaned_data.get('username')
			password_var=form.cleaned_data.get('password1')
			user=authenticate(username=username_var,password=password_var)

			login(request,user) 
			return redirect ('hshome3')
	else:
		form=UserRegisterForm(request.POST)
		extend_form=ExtendedUserForm(request.POST,request.FILES)

	context={"form":form,"extend_form":extend_form}
	return render(request,'hsregistration.html',context)


class AddDepartmentView(CreateView):
	template_name='Department.html'
	form_class=AddDepartmentForm
	success_url='/master/adhhome/'

class StaffView(CreateView):
	template_name='staff.html'
	form_class=StaffRegistrationForm
	success_url='/master/hshome3/'

def StaffView(request):
	if request.method=="POST":
		form=StaffUserRegisterForm(request.POST)
		extend_form=StaffRegistrationForm(request.POST,request.FILES)

		if form.is_valid() and extend_form.is_valid():
			user=form.save()
			extended_profile=extend_form.save(commit=False)
			extended_profile.user=user
			extended_profile.save()

			username_var=form.cleaned_data.get('username')
			password_var=form.cleaned_data.get('password1')
			user=authenticate(username=username_var,password=password_var)

			login(request,user)
			return redirect ('hshome3')
	else:
		form=StaffUserRegisterForm(request.POST)
		extend_form=StaffRegistrationForm(request.POST,request.FILES)

	context={"form":form,"extend_form":extend_form}
	return render(request,'staff.html',context)

class StaffListView(ListView):
	template_name='staffview.html'
	model=StaffRegistrationModel
	context_object_name='staff'

class UserView(ListView):
	template_name='userview.html'
	model=UserRegisterModel
	context_object_name='user'

import requests
class UserLogin(View):
	def get(self,request):
		form=AuthenticationForm()
		context={'form':form}
		return render(request,'hslogin.html',context)

	def post(self,request):
		username=request.POST.get('username')
		password=request.POST.get('password')
		recaptcha_response = request.POST.get('g-recaptcha-response')
		data = {
			'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
			'response': recaptcha_response
			}
		r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
		result = r.json()
		if result['success']:
			user=authenticate(username=username,password=password)
			login(request,user,backend='django.contrib.auth.backends.ModelBackend')

		# user=authenticate(username=username,password=password)
			if user is not None :
				login(request,user)
				if user.is_superuser == True and user.is_staff == True:
					return redirect('adhhome')
			if user.is_staff == True and user.is_superuser == False:
				return redirect('staffhome')
				if user.is_staff == False and user.is_superuser == False:
					return redirect ('hshome3')
			else:
				form=AuthenticationForm()
				context={'form':form}
				return render(request,'hslogin.html',context)

def logout_request(request):
	logout(request)
	return redirect("hshome3")

#edit
class EditView(UpdateView):
	template_name='edit.html'
	model=UserRegisterModel
	fields=['age','address','id_card']
	success_url='/master/hshome3/'

class StaffEditView(UpdateView):
	template_name='staffedit.html'
	model=StaffRegistrationModel
	fields=['first_name','age','address','profile']
	success_url='/master/hshome3/'

class DepartmentView(ListView):
	template_name='departmentview.html'
	model=AddDepartmentModel
	context_object_name='department'

class UserDetailView(DetailView):
	template_name='userdetail.html'
	model=UserRegisterModel

class AddAppoinmentView(View):
	template_name='addappoinment.html'
	def get(self,request):
		context={'form':AddAppoinmentForm}
		return render(request,self.template_name,context)

	def post(self,request):
		user_var=request.user
		department_var=AddDepartmentModel.objects.get(id=request.POST.get('department'))
		doctorname_var=StaffRegistrationModel.objects.get(id=request.POST.get('doctorname'))
		appoinment_time_var=request.POST.get('appoinment_time')appoinment_time
		appoinment_date_var=request.POST.get('appoinment_date')
		AddAppoinmentModel.objects.create(user=user_var,department=department_var,
			doctorname=doctorname_var,appoinment_time=appoinment_time_var,appoinment_date=appoinment_date_var)
		return redirect('recent')

class AppoinmentListView(ListView):
	template_name='appoinmentview.html'
	model=AddAppoinmentModel
	context_object_name='appoinment'

class AppoinmentStaffListView(View):
	template_name='staffappoinmentlist.html'

	def get(self,request):
		
		cur_user=int(request.user.id)
		context={
		'data':AddAppoinmentModel.objects.filter(doctorname=cur_user)
		}

		return render(request,self.template_name,context)

class AppoinmentEditView(UpdateView):
	template_name='appoinmentedit.html'
	model=AddAppoinmentModel
	fields=['department','doctorname','appoinment_time','appoinment_date']
	success_url='/master/addappoinmentview/'

class ShowRecentAppoinment(View):
	template_name='ShowRecentAppoinment.html'

	def get(self,request):
		cur_user=request.user
		data=AddAppoinmentModel.objects.filter(user=cur_user).last()
		print(data)
		doctor_var=data.doctorname
		department_var=data.department
		print(department_var)
		date_var=data.appoinment_date
		time_var=data.appoinment_time
		dept_data=AddDepartmentModel.objects.get(dept_name=department_var)
		print(dept_data)
		fees_var=dept_data.fees
		print(fees_var)

		context={
		'user':cur_user,
		'doctorname':doctor_var,
		'department':department_var,
		'date':date_var,
		'time':time_var,
		'fees':fees_var
		}
		return render(request,self.template_name,context)


class SearchView(View):
    template_name = 'appoinmentview2.html'
    def get(self,request):
    	context={'form':AddAppoinmentForm}
    	return render(request,self.template_name,context)


    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = Article.objects.filter(title__contains=query)
          result = postresult
       else:
           result = None
       return result


class AddLeaveView(View):
	template_name='addleave.html'
	def get(self,request):
		context={'form':AddLeaveForm}
		return render(request,self.template_name,context)

	def post(self,request):
		user_var=request.user
		department_var=AddDepartmentModel.objects.get(id=request.POST.get('department'))
		name_var=request.POST.get('name')
		leave_type_var=request.POST.get('leave_type')
		Start_date_var=request.POST.get('Start_date')
		end_date_var=request.POST.get('end_date')
		# approvel_status_var=request.POST.get('approvel_status')
		AddLeaveViewModel.objects.create(user=user_var,department=department_var,name=name_var,
			leave_type=leave_type_var,Start_date=Start_date_var,end_date=end_date_var)
		return redirect('staffhome')

class LeaveListView(ListView):
	template_name='leaveview.html'
	model=AddLeaveViewModel  
	context_object_name='leave'


class LeaveDetailView(DetailView):
	template_name='leavedetail.html'
	model=AddLeaveViewModel

class LeaveEditView(UpdateView):
	template_name='leaveedit.html'
	model=AddLeaveViewModel
	fields=['name','Start_date','end_date','approvel_status']
	success_url='/master/leaveview'


class LeaveCurrentView(View):
	template_name='currentleave.html'

	def get(self,request):
		cur_user=request.user
		context={'cur_list':AddLeaveViewModel.objects.filter(user=cur_user)}
		return render(request,self.template_name,context)

# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
	auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


class PaymentView(View):
	template_name="payment.html"

	def get(self,request):
		data=AddAppoinmentModel.objects.last()
		dept_var=data.department
		dept_data=AddDepartmentModel.objects.get(dept_name=dept_var)
		fees_var=dept_data.fees
		amount=int(fees_var)*100
		currency = 'INR'
		# amount = 20000  # Rs. 200
 
		# Create a Razorpay Order
		razorpay_order = razorpay_client.order.create(dict(amount=amount,
			currency=currency,payment_capture='0'))
 
		# order id of newly created order.
		razorpay_order_id = razorpay_order['id']
		callback_url = '/master/paymenthandler/'
 
		# we need to pass these details to frontend.
		context = {'amount_rupee':fees_var}
		context['razorpay_order_id'] = razorpay_order_id
		context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
		context['razorpay_amount'] = amount
		context['currency'] = currency
		context['callback_url'] = callback_url
 
		return render(request,self.template_name, context=context)
 
 

@csrf_exempt
def paymenthandler(request):
 
	# only accept POST request.
	if request.method == "POST":
		try:
           
			# get the required parameters from post request.
			payment_id = request.POST.get('razorpay_payment_id', '')
			razorpay_order_id = request.POST.get('razorpay_order_id', '')
			signature = request.POST.get('razorpay_signature', '')
			params_dict = {
				'razorpay_order_id': razorpay_order_id,
				'razorpay_payment_id': payment_id,
				'razorpay_signature': signature
			}
 
			# verify the payment signature.
			result = razorpay_client.utility.verify_payment_signature(
				params_dict)
			if result is None:
				# amount = 20000  # Rs. 200
				data=AddAppoinmentModel.objects.last()
				dept_var=data.department
				dept_data=AddDepartmentModel.objects.get(dept_name=dept_var)
				fees_var=dept_data.fees
				amount=int(fees_var)*100
				data.payment_status=True
				data.save()
				try:
 
					# capture the payemt
					razorpay_client.payment.capture(payment_id, amount)
 
					# render success page on successful caputre of payment
					return render(request, 'paymentsuccess.html')
				except:
 
					# if there is an error while capturing payment.
					return render(request, 'paymentfail.html')
			else:
 
				# if signature verification fails.
				return render(request, 'paymentfail.html')
		except:
 
			# if we don't find the required parameters in POST data
			return HttpResponseBadRequest()
	else:
		# if other than POST request is made.
		return HttpResponseBadRequest()



def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password_reset.html", context={"password_reset_form":password_reset_form})




# def subscribe(request):
# 	sub = forms.Subscribe()
# 	if request.method == 'POST':
# 		sub = forms.Subscribe(request.POST)
# 		subject = 'Welcome'
# 		message = 'Hope you are enjoying your Day'
# 		recepient = str(sub['Email'].value())
# 		send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently =False)
# 		return render(request, 'success.html', {'recepient': recepient})
# 		render(request, 'index.html', {'form':sub})
