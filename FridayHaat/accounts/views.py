from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from .forms import LoginForm, RegistrationForm


def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
	    "form" : form
	}
	print("User Logged In")
	#print(request.user.is_authenticated) 
	# as user is an object and not a method/function so cannot use is_authenticated()
	next_ = request.GET.get('next')
	next_post = request.POST.get('next')
	redirect_path = next_ or next_post or None
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			try:
				del request.session['guest_email_id']
			except:
				pass
			if is_safe_url(redirect_path, request.get_host()):
				return redirect(redirect_path)
			else:
				return redirect("home")
		else:
			print("Error")
	return render(request, "accounts/login.html", context)

user = get_user_model()	
def register_page(request):
	form = RegistrationForm(request.POST or None)
	context = {
	    "form" : form
	}	
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		new_user = user.objects.create_user(username, email, password)
		print(new_user)
		return redirect("login")
	return render(request, "accounts/register.html", context)
