from django.urls import path, include
from .views import vehicleViewset
from rest_framework import routers

#define the router:
router = routers.DefaultRouter()

#define the router path and viewset to be used:
router.register(r'api/vehicles',vehicleViewset)

#specify the url paths for rest_framework:


urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]