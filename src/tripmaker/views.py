from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegisterForm, LoginForm

def index(request):
	context={
		"hi":"hello"
	}
	return render(request, "index.html", context)
	# return HttpResponse("HELLo")


User=get_user_model()

def login_user(request):

	if request.user.is_authenticated:
		return HttpResponseRedirect("/home/")
	else:
		# form=LoginForm(request.POST or None)

		# context={
		# 	"message":"LOG-IN",
		# 	"form":form
		# }

		# if form.is_valid():
		# 	username=form.cleaned_data.get("username")
		# 	password=form.cleaned_data.get("password")

		# 	user=authenticate(request, username=username, password=password)
		# 	print(user)

		# 	if user is not None:
		# 		login(request, user)
		# 		return HttpResponseRedirect("/home/")
		# 	else:
		# 		print("There is an error in your login information")

		context={
			"message":"LOG-IN",
		}

		if request.method == "POST":
			print("Log In Will Be")
			username=request.POST.get('username')
			password=request.POST.get('password')

			print(username)
			print(password)

			user=authenticate(request, username=username, password=password)
			print(user)

			if user is not None:
				login(request, user)
				return HttpResponseRedirect("/home/")
			else:
				print("There is an error in your login information")


		return render(request, "login.html", context)


def signup_user(request):

	if request.user.is_authenticated:
		print("Auth")

		return HttpResponseRedirect("/home/")

	else:
		print("Not Auth")

		form=RegisterForm(request.POST or None)

		context = {
			"message":"SIGN-UP",
			"form":form
		}

		if form.is_valid():		
			# print(form.cleaned_data)

			username=form.cleaned_data.get("username")
			email=form.cleaned_data.get("email")
			password=form.cleaned_data.get("password")

			new_user = User.objects.create_user(username, email, password)
			user=authenticate(request, username=username, password=password)
			login(request, user)

			return HttpResponseRedirect("/home/")

		return render(request, "signup.html", context)

def logout_user(request):
	logout(request)
	return HttpResponseRedirect("/")


def home(request):
	context = {
		"message" : "My Home"
	}
	return render(request, 'home.html', context)
