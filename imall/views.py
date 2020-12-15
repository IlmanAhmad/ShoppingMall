from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from imall.models import USERPROFILE, Product
from math import ceil

# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# import json






# Create your views here.

def home(request):
    """ This function will handle home page related items"""
    all_prods = Product.objects.all()
    n = len(all_prods)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_slides': nSlides, 'range': range(1,nSlides), 'all_prods': all_prods}
    return render(request, 'home.html', params)


def handlesignup(request):
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
    else:
        return HttpResponse('404 - Not found')


def handlelogin(request):
    if request.method == "POST":
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Your login is successful. Happy Shopping!")
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


def about(request):
    return render(request, 'aboutus.html')


    
def cart(request):
    return render(request, 'cart.html')



def orders(request):
    return render(request, 'orderstatus.html')












        

    

