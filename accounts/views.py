from django.shortcuts import render
from django.contrib.auth.models import User, auth
# Create your views here.


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']

        if User.objects.filter(first_name=first_name).exists():
            print("name taken")


        user = User.objects.create_user(first_name=first_name, last_name=last_name, password=password)
        user.save()
        print('user created')
        return redirect('/')

    else:

        return render(request, 'register.html')
