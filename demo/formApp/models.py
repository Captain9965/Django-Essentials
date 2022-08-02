from django.db import models as m

# Create your models here.

class vehicleModels(m.Model):

    
    model = m.CharField(max_length=100)
    engine_capacity = m.IntegerField()
    description = m.TextField()
    last_modified = m.DateTimeField(auto_now_add=True)
    image = m.ImageField(upload_to = "images/")

    #useful for debugging purposes to represent the object instances.
    def __str__(self):
        return self.title
