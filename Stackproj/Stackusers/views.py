from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterEmail


# Create your views here.
def register(request):
	if request.method == "POST":
		# form = UserCreationForm(request.POST)
		form = UserRegisterEmail(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}. Login now')
			return redirect('Stackbase:home')
	else:
		#form = UserCreationForm()
		form = UserRegisterEmail()

	return render(request, 'Stackusers/register.html', {'form' : form})


