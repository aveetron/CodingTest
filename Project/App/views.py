from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from todo import urls


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return redirect('/all-todos')
        else:
            return HttpResponse('username or password is incorrect')
    return render(request, 'auth/login.html', {})


def user_logout(request):
    logout(request)
    return redirect('/login')


def user_signup(request):
    form = UserCreationForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password_one = request.POST.get('password1')
        password_two = request.POST.get('password2')
        if password_one == password_two:
            user = User.objects.create_user(username, '', password_one)
            user.save()
            return redirect('/login')
        else:
            return HttpResponse('Password didnot matched!')


    return render(request, 'auth/signup.html', {'forms': form})

