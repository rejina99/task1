from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User = auth.authenticate(username=username, password=password)
        if User is not None:
            auth.login(request, User)
            return redirect("/")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']

        if User.objects.filter(first_name=first_name).exists():
            messages.info(request, 'name taken')


        user = User.objects.create_user(first_name=first_name, last_name=last_name, password=password)
        user.save()
        print('user created')
        return redirect('/')

    else:

        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
