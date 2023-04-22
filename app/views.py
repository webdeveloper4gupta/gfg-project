from django.shortcuts import render

# Create your views here.
def home(request):
          return render(request,"index.html")

def laptop_price(request):
          return render(request,"laptop_price.html")

def phone_price(request):
          return render(request,"phone_price.html")

def car_price(request):
          return render(request,"car_price.html")

def house_price(request):
          return render(request,"house_price.html")
def about(request):
          return render(request,"Aboutus.html")