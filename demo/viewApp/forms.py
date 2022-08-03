from array import array
from django import forms as f
from .models import vehicleModels as v

class vehicleModelForm(f.ModelForm):
    class Meta:
        model = v
        fields = ('model', 'engine_capacity')

class AddForm(f.ModelForm):
    class Meta:
        model = v
        fields = ('model', 'engine_capacity')
        widgets = {
            'model': f.TextInput(attrs={'class': 'form-control'}),
            'engine_capacity' : f.TextInput(attrs={'class': 'form-control'})
        }