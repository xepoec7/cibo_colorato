from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

def login_page(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Sie sind eingelogt als {username}.")
				return redirect('frontend:home')
			else:
				messages.error(request, 'Benutzername oder Passwort ist falsch...')
		else:
			messages.error(request, 'Benutzername oder Passwort ist falsch...')
	form = AuthenticationForm()
	return render(request, 'login.html', {'login_form': form})


def logout_request(request):
	logout(request)
	messages.info(request, 'Sie haben sich ausgelogt.')
	return redirect('konto:login')