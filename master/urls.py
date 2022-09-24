from django.urls import path,re_path
# from master.views import HomeView,adduser,ProjectView,DepartmentView,StaffView,UserView,UserLogin,logout,AboutView,EditView,StaffEditView,LoginView,RegistrationView,ForgottenView,ContactView,UserDetailView
from master.views import*
from master import views

urlpatterns = [
	path('home/',HomeView.as_view(),name='home',),
    path('register/', views.adduser, name='reg'),
    path('hshome3/',ProjectView.as_view(),name='hshome3'),
    # path('hslogin/',LoginView.as_view(),name='hslogin'),
    # path('hsregistration/',views.RegistrationView,name='hsregistration'),
    path('hsforgotten/',ForgottenView.as_view(),name='hsforgotten'),
    path('hscontact/',ContactView.as_view(),name='hscontact'),
    path('hsabout/',AboutView.as_view(),name='hsabout'),
    path('Department/',AddDepartmentView.as_view(),name='Department'),
    path('staff/',views.StaffView,name='staff'),
    path('staffview/',StaffListView.as_view(),name='stafflist'),
    path('userview/',UserView.as_view(),name='user'),
    path('hslogin/',UserLogin.as_view(),name='hslogin'),
    path('logout/', views.logout_request, name='logout'),
    re_path(r'^edit/(?P<pk>\d+)$',EditView.as_view(),name='edit'),
    re_path(r'^staffedit/(?P<pk>\d+)$',StaffEditView.as_view(),name='staffedit'),
    path('departmentview/',DepartmentView.as_view(),name='department'),
    re_path(r'^userdetail/(?P<pk>\d+)$',UserDetailView.as_view(),name='userdetail'),
    # path('index/',IndexView.as_view(),name='index'),
    path('addappoinment/',AddAppoinmentView.as_view(),name='appoinment'),
    path('addappoinmentview/',AppoinmentListView.as_view(),name='appoinmentview'),
    re_path(r'^appoinmentedit/(?P<pk>\d+)/$',AppoinmentEditView.as_view(),name='appoinmentedit'),
    # path('addappoinmentview2/',SearchView.as_view(),name='appoinmentview2'),
    path('addleave/',AddLeaveView.as_view(),name='addleave'),
    path('leaveview/',LeaveListView.as_view(),name='leaveview'),
    re_path(r'^leavedetail/(?P<pk>\d+)$',LeaveDetailView.as_view(),name='leavedetail'),
    re_path(r'^leaveedit/(?P<pk>\d+)$',LeaveEditView.as_view(),name='leaveedit'),
    path('currentleave/',LeaveCurrentView.as_view(),name='currentleave'),
    path('recent/appoinment/',ShowRecentAppoinment.as_view(),name='recent'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('pay/', PaymentView.as_view(), name='pay'),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path('adhhome/',IndexView.as_view(),name='adhhome'),
    path('staffhome/',StaffHomeView.as_view(),name='staffhome'),
    path('appoinment/staff/view/',AppoinmentStaffListView.as_view(),name='appoinmentstaffview'),
    ]


