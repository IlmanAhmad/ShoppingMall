from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from imall.models import USERPROFILE, Product

# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from math import ceil
# import json






# Create your views here.
def basic(request):
    """Create a new user using custom user model we created using below function"""
    USER = USERPROFILE.objects.all()
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        if password1 == password2:
            password = request.POST.get('password1', '')
        else:
            messages.error(request, "Account not created.Entered Password does not match with confirm password")
            return redirect("mall:home")
        newuser = USERPROFILE.objects.create_user(email=email, name=name, password=password)
        messages.success(request, "Your registeration has been successfull. Please login!")
        return redirect("mall:home")

            
    return render(request, 'basic.html')

def handlelogin(request):
    if request.method == "POST":
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Your login is successfull. Happy Shopping!")
            return redirect("mall:home")
        else:
            messages.error(request, "Invalid id or password")
            return redirect("mall:home")
    else:
        return HttpResponse('404 - Not found')


def handlelogout(request):
    logout(request)
    messages.success(request, "Your have successfully logged out")
    return redirect("mall:home")
    return HttpResponse('404 - Not found')









        

    

