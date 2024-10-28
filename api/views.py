from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
            messages.success(request, 'Registration successful!')
            return redirect('/login/')  # Asegúrate de que esta ruta exista
        except Exception as e:
            messages.error(request, 'Registration failed. Please try again.')
            return redirect('/register/')  # Asegúrate de que esta ruta exista
    return render(request, 'register.html')  # Asegúrate de que esta plantilla exista


    