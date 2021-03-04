from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

#Username= Nik-586 and password= coen6311
# Create your views here.


def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "index.html")

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        #check if the credentials entered by the user are correct or not
        user = authenticate(username=username, password=password)

        if user is not None:
            #Backend authentication for creds
            return render(request,"index.html")
        else:
            # NO Backend authentication for creds
            return render(request, "login.html")

    return render(request, "login.html")


def logoutUser(request):
    logout(request)
    return redirect("/login")
