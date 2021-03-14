from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from Psychbudapp.models import User
from Psychbudapp.forms import UserForm

# Create your views here.
def base_view(request):
    return render(request,'star/Base.html')

def login_view(request):
    return render(request,'registration/login.html')

def logout_view(request):
    return render(request,'star/logout.html' )

def form_view(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')

    return render(request,'star/register.html',{'form':form})



