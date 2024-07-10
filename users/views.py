from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'auth/login.html', context={"message": "Password yoki Username xato"})

    return render(request, 'auth/login.html')


def regester_view(request):
    if request.method == 'POST':
        first_name = request.POST['name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password != password1:
            return render(request, 'auth/regester.html', context={"message_password": "Error Password!!!"})
        else:
            if User.objects.filter(username=username).exists():
                return render(request, 'auth/regester.html', context={"message": "Bunday usernamelik foydalanuvchi mavjud"})

            new_user = User(first_name=first_name, last_name=last_name, email=email, username=username)
            new_user.set_password(password)
            new_user.save()
            return redirect('login')

    return render(request, 'auth/regester.html')


def logout_view(request):
    logout(request)
    return redirect('login')


