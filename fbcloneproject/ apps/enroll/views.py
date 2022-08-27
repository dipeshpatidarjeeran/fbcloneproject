from django.shortcuts import render
from django.contrib import messages
from django.views.generic import CreateView
# Create your views here.
from .forms import SignupForm
def sign_up(request):
	if request.method=='POST':
		fm=SignupForm(request.POST)
		if fm.is_valid():
			messages.success(request,'Account Created Successfully !!')
			fm.save()
	else:
		fm=SignupForm()
	return render(request,'enroll/signup.html',{'form':fm})

'''class SignupFormView(CreateView):
	form_class=SignupForm
	templale_name='enroll/signup.html'
	def get'''