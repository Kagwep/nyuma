from urllib.parse import urlparse
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.Home, name= 'home'),
    path("property/",views.ViewProperty, name='property'),
    path("property/int<pk>/",views.ViewProp, name='property-view'),
    path("property/int<pk>/",views.ViewCar, name='car-view'),
    path("cars/",views.ViewCars, name='cars')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

