from django.shortcuts import render, redirect
from .forms import Signup ,Login
from django.contrib.auth import login , logout,authenticate
# Create your views here.

def user_signup(request):
    form = Signup()
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("/users/signin/")
    context = {
        "form":form,
    }
    return render(request, 'signup.html', context)

def user_signin(request):
    form = Login()
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('/users/signin/')

    context = {
        "form":form
    }
    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    return redirect("/users/signin/")