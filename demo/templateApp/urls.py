
from django.urls import path
from .views import templates

urlpatterns = [
    #map the url to the welcome function.
    path('templatesIntro/',templates.intro),
]