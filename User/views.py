from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.contrib import messages
from django import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.success(request, 'Username or password was wrong, try again!')
			return redirect('login')
	else:
		return render(request, 'login_view.html', {})

def logout_view(request):
	logout(request)
	messages.success(request, "You're logged out")
	return redirect('login')

def register_view(request):
	if request.method == 'POST':
		account = RegisterUserForm(request.POST)
		if account.is_valid():
			account.save()
			messages.success(request, "You're succefully registred")
			return redirect('login')
	else:
		account = RegisterUserForm()
	return render(request, 'register_view.html', {'account' : account})

@login_required
def home_view(request):
	return render(request, 'home_view.html')

def redirect_login(request):
	return redirect('login/')