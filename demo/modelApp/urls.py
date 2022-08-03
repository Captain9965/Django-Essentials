from django.urls import path
from .views import createModel, listObjects, updateModel

urlpatterns = [
    #map the url to the welcome function.
    path('model/createmodel/',createModel),
    path('model/listobjects/',listObjects),
    path('model/updateobject/<id>/',updateModel)
]