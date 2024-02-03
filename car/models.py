from django.db import models
from car_brand.models import CarBrand
from django.contrib.auth.models import User

# Create your models here.
class CarModel(models.Model):
    car_name = models.CharField(max_length=100)
    car_price = models.CharField(max_length=100)
    car_brand_name = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.IntegerField(default=20)
    image = models.ImageField(upload_to='car/media/uploads/', blank=True , null=True)
    
    
    def __str__(self):
        return self.car_name
    
    
class Comment(models.Model):
    post = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) # j somoy ei class er object creae hobe thikon current time ta rekhe dibe
    
    def __str__(self):
        return f'coomment by {self.name}'
    
    
class Cart(models.Model):
    # car_name = models.CharField(max_length=55) 
    # car_description = models.TextField() 
    # car_price = models.CharField(max_length=55) 
    # car_brand = models.CharField(max_length=155) 
    # car_image = models.ImageField(upload_to='car/media/uploads/', blank=True, null=True) 
    user = models.OneToOneField(User,on_delete = models.CASCADE,null = True,blank = True)
    car = models.ManyToManyField(CarModel)
    purchase_date = models.DateTimeField(auto_now_add=True)
    
    
    
    # def __str__(self):
    #     return f'{self.user.username}'
    
    
    
