import re
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import Profile


def register_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            hashed = make_password(password)
            base_username = re.sub(r'\W+','',first_name).lower()
            now = datetime.now().strftime('%Y%m%d%H%M%S')
            username = f"{base_username}{now}"

            # Create and save the new Level object
            new_user = User(username=username, first_name=first_name, last_name=last_name, email=email, password=hashed)
            new_user.save()

            user_id = new_user.id
            Profile.objects.create(user_id=user_id, phone=phone)

            user = authenticate(email=email, password=password)
            login(request, user)

            return redirect('dashboard:dashboard')
    return render(request, 'accounts/signup.html')



def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('dashboard:dashboard')
        else:
            messages.success(request, ('There was an error logging in. Try again later..'))
            return render(request,'accounts/login.html', {})
    else:
        return render(request, 'accounts/login.html', {})


def logout_view(request):
    logout(request)
    return redirect('accounts:login')