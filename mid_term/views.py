from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm
from django.contrib.auth.decorators import login_required
from  car.models import CarModel
from car_brand.models import CarBrand


def home(request,car_brand_slug=None):
    data = CarModel.objects.all()
    
    if car_brand_slug is not None:
        carbrand = CarBrand.objects.get(slug = car_brand_slug)
        data = CarModel.objects.filter(car_brand_name = carbrand)
    brand = CarBrand.objects.all()
    return render(request,'home.html',{'data':data,'brand':brand})



def usersignup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.SignUpForm(request.POST)
            if form.is_valid():
                messages.success(request,'Account Create Successfully')
                form.save()
                return redirect('homepage')
        else:
            form = forms.SignUpForm()
        return render(request,'signup.html',{'form':form})
    else:
        return redirect('homepage')





def userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username = username, password = userpass)
            if user is not None:
                messages.success(request,'Login Successfully')
                login(request,user)
                return redirect('homepage')
            else:
                messages.success(request,'Login information incorrect')
                return redirect('signuppage')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html',{'form':form})
    



@login_required
def userlogout(request):
    logout(request)
    messages.success(request,'Log Out Successfully')
    return redirect('loginpage')


