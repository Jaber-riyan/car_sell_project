from django.shortcuts import render,redirect,get_object_or_404
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models
from django.views.generic import DetailView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse


# Create your views here.


@login_required
def addcar(request):
    if request.method == 'POST':
        form = forms.CarForm(request.POST)
        if form.is_valid():
            messages.success(request,'Car Add Successfully')
            form.save()
            return redirect('homepage')
    else:
        form = forms.CarForm()
    return render(request,'addcar.html',{'form':form})



# def DetailViewOfCar(request,pk):
#     data = models.CarModel.objects.get(id=pk)
#     return render(request,'car_detail.html',{'object':data})
    
class DetailViewOfCar(DetailView):
    model = models.CarModel
    pk_url_kwarg = 'pk'
    template_name = 'car_detail.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            comment_form.instance.name = request.user.username
            comment_form.instance.email = request.user.email
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        # print(self.pk_url_kwarg)

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context




@login_required    
def buynow(request,id):  
    one_car = models.CarModel.objects.get(id=id) 
    if request.user: 
        data,purch_car = models.Cart.objects.get_or_create(user=request.user)
        
        data.car.add(one_car)
        # messages.success(request,'Add Cart Successfully') 
    # one_car.quantity -=1
        if(one_car.quantity==0):
            messages.success(request,'This Car is Out Of Stock Buy Another One')
        else:
            messages.success(request,'Add Cart Successfully')
            one_car.quantity -=1
            
    one_car.save()
    return redirect('homepage')
            
 
   

@login_required
def profile(request,id):
    car = models.CarModel.objects.get(id=id)
    data = get_object_or_404(models.Cart,user = request.user)
    print(data)
    return render(request,'profile.html',{'data':data})






@login_required
def updateprofile(request):
    if request.method == 'POST':
        profile_form = forms.UserChangeForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'Profile Updated Successfully')
            return redirect('updateprofile')
    else:
        profile_form = forms.UserChangeForm(instance = request.user)
    return render(request, 'update_profile.html',{'form' : profile_form, 'type' : 'Update Profile'})


    


@login_required
def passchange1(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(request.user, data = request.POST)
        if pass_form.is_valid():
            pass_form.save()
            messages.success(request,'Password Updated successfully')
            update_session_auth_hash(request, pass_form.user)
            return redirect('profile')
    else:
        pass_form = PasswordChangeForm(request.user)
    return render(request, 'pass_change.html',{'form' : pass_form, 'type' : 'Using Old Password Change The Password : '})
    


 