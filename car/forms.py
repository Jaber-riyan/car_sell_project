from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class CarForm(forms.ModelForm):
    class Meta:
        model = models.CarModel
        fields = '__all__'




        
class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['name','email','body']
        
        
        
class UserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
        