
from django.db import models as m
from django.template.defaultfilters import slugify  


# Create your models here.

class vehicleModels(m.Model):

    
    model = m.CharField(max_length=100)
    engine_capacity = m.IntegerField()
    last_modified = m.DateTimeField(auto_now_add=True)
    slug = m.SlugField(null=True)

    #useful for debugging purposes to represent the object instances.
    def __str__(self):
        return self.model