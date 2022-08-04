from django.urls import path
from .views import createModel, listObjects, updateModel, slugView

urlpatterns = [
    #map the url to the welcome function.
    path('model/createmodel/',createModel),
    path('model/listobjects/',listObjects),
    path('model/updateobject/<id>/',updateModel),
    path('model/<slug>/',slugView),
]