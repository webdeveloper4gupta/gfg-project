
from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name='home'),
   path('laptop/',views.laptop_price,name='laptop_price')
   ,path('phone/',views.phone_price,name='phone_price'),
   path('car/',views.car_price,name='car_price'),
   path('house/',views.house_price,name="house_price"),
   path('aboutus/',views.about,name='about')
]
