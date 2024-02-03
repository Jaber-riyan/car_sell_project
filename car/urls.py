from django.urls import path
from .views import addcar, DetailViewOfCar,buynow,updateprofile,profile,passchange1

urlpatterns = [
    path('addcar/', addcar, name='addcarpage'),
    
    path('detailview/<int:pk>/', DetailViewOfCar.as_view(), name='detailview'),
    
    path('buynow/<int:id>/',buynow,name='buynow'),
    path('updateprofile/',updateprofile,name='updateprofile'),
    path('profile/<int:id>/',profile,name='profile'),
    path('passchange1/',passchange1,name='passchange1'),
]
