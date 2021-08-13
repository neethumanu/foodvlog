from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['firstname']
        email = request.POST['email']
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']

        user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
        user.save()
        print("user created")
        return redirect('/')
    else:
        return render(request, 'registration.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
