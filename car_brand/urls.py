from django.urls import path 
from . import views

urlpatterns = [
    path('addcarbrand/',views.addcarbrand,name='addcarbrandpage'),
]