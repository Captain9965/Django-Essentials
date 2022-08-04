from django.db import models as m
from django.dispatch import receiver
from django.db.models.signals import pre_save

from django.template.defaultfilters import slugify
from demo.utils import unique_slug_generator
from django.core.exceptions import ValidationError


""" custom validation functions: """

def validate_engine_capacity(value):
    print(value)
    if(value < 100 or value > 12000):
        raise ValidationError("Value out of bounds")
    return value


""" model choices consisting of a tuple of tuples where the first value is the actual value and the second, the human readable format:"""
COLOUR_CHOICES = (
    ("blue", "Blue"), 
    ("red", "Red"),
    ("black", "Black")
)

# Create your models here.

class vehicleModels(m.Model):

    
    model = m.CharField(max_length=100)
    engine_capacity = m.IntegerField(validators=[validate_engine_capacity])
    last_modified = m.DateTimeField(auto_now_add=True)
    colour = m.CharField(choices= COLOUR_CHOICES,
                        max_length=20,
                        default= 'Black')
    slug = m.SlugField(null=True)

    #useful for debugging purposes to represent the object instances.
    def __str__(self):
        return self.model

""" This is a signal to generate slugs: """

@receiver(pre_save, sender = vehicleModels)
def pre_save_receiver(sender, instance,*args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


