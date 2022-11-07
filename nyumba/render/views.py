
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Cars, Property, SubCategories, SubCategoriesCars



def Home(request):
    properties = Property.objects.all()
    subcat = SubCategories.objects.all()
    context = {"properties":properties,"subcat":subcat}
    return render(request,'home.html',context)


def ViewProperty(request):

    

    return render(request,'properties.html')

def ViewCars(request):

    cars = Cars.objects.all()
    subcatcars = SubCategoriesCars.objects.all()
    context = {"cars":cars, "subcatcars":subcatcars}
    return render(request,'cars.html',context)


def ViewCar(request,pk):
    car = Cars.objects.get(pk=pk)
    context = {"car":car}
    return render (request,'car-view.html',context)

def ViewProp(request,pk):
    prop = Property.objects.get(pk=pk)
    context = {"prop":prop}
    return render (request,'property-view.html',context)