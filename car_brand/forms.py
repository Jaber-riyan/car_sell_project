from django import forms
from . import models

class CarBrandForm(forms.ModelForm):
    class Meta:
        model = models.CarBrand
        fields = ['brand_name','brand_owner',]