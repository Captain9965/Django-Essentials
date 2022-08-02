from django.forms import ModelForm
from django.urls import path
from .views import welcome, forms

urlpatterns = [
    #map the url to the welcome function.
    path('conventionalForm/',forms.conventionalForm),
    path('modelForm/',forms.modelForm),
    path('djangoForm/',forms.djangoForm),
]