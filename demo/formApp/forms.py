from django import forms as f
from .models import vehicleModels as v

class vehicleForm(f.Form):
    """
        one can use the initial attribute to add initial data. 
        
    """
    model = f.CharField(max_length=100)
    engine_capacity = f.IntegerField(max_value=8000, help_text="Enter the engine capacity in cc", label="Engine capacity")
    colour = f.CharField(max_length=100)
    password = f.CharField(widget=f.PasswordInput())
    """ used to use the date-time widget..."""
    date = f.DateField(widget=f.SelectDateWidget)
class vehicleModelForm(f.ModelForm):
    class Meta:
        model = v
        fields = "__all__"


