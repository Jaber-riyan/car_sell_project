from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def addcarbrand(request):
    if request.method == 'POST':
        form = forms.CarBrandForm(request.POST)
        if form.is_valid():
            messages.success(request,'Car Brand Add Successfully')
            form.save()
            return redirect('homepage')
    else:
        form = forms.CarBrandForm()
    return render(request,'addcar.html',{'form':form})