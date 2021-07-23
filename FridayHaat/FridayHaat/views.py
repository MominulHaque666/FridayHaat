from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm

def home_page(request):
	# print(request.session.get("first_name", "Unknown"))
	context = {
	    "title" : "<<<<< Friday Haat >>>>>",
	    "content" : "Welcome to the Home Page",

	}
	if request.user.is_authenticated:
		context["premium_content"] = "Happy Shopping"
	return render(request, "home_page.html", context)

def about_page(request):
	context = {
	    "title" : "About Page",
	    "content" : "Welcome to the About Page"
	}
	return render(request, "home_page.html", context)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
	    "title" : "Contact Page",
	    "content" : "Hey, Welcome to the Contact Page",
	    "form" : contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	# if request.method == "POST":
	# 	print(request.POST)
	# 	print(request.POST.get('fullname'))
	# 	print(request.POST.get('email'))
	# 	print(request.POST.get('content'))
	return render(request, "contact/view.html", context)

# def login_page(request):
# 	form = LoginForm(request.POST or None)
# 	context = {
# 	    "form" : form
# 	}
# 	print("User Logged In")
# 	#print(request.user.is_authenticated) 
# 	# as user is an object and not a method/function so cannot use is_authenticated()
# 	if form.is_valid():
# 		print(form.cleaned_data)
# 		username = form.cleaned_data.get("username")
# 		password = form.cleaned_data.get("password")
# 		user = authenticate(request, username=username, password=password)
# 		print(user)
# 		if user is not None:
# 			login(request, user)
# 			return redirect("home")
# 		else:
# 			print("Error")
# 	return render(request, "auth/login.html", context)

# user = get_user_model()	
# def register_page(request):
# 	form = RegistrationForm(request.POST or None)
# 	context = {
# 	    "form" : form
# 	}	
# 	if form.is_valid():
# 		print(form.cleaned_data)
# 		username = form.cleaned_data.get("username")
# 		email = form.cleaned_data.get("email")
# 		password = form.cleaned_data.get("password")
# 		new_user = user.objects.create_user(username, email, password)
# 		print(new_user)
# 	return render(request, "auth/register.html", context)

def home_page_old(request):
	return HttpResponse("Hello CSE327 Group Mates!!!")
    