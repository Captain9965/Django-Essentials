from logging import exception
import re
from django.shortcuts import render
from django.http import HttpResponse

""" used when rendering multiple forms in a single page """

from django.forms import formset_factory, modelformset_factory

from .forms import vehicleForm, vehicleModelForm
# Create your views here.
class welcome():
    def welcome_to_django(request):
        return HttpResponse("Welcome to Django man! Happy coding!")
class forms():
    def modelForm(request):
        context = {}

        """
            One can pass a dictionary containing the form fields as keys to the form to be rendered as initial data

        """
        context['form'] = vehicleModelForm()
        return render(request, "djangoForm.html", context)
    def djangoForm(request):

        """
            This is a context dictionary to pass data to the template:

        """
        context = {}
        context['form'] = vehicleForm()
        return render(request, "djangoForm.html", context)
    def conventionalForm(request):
        print(request.POST)
        try:
            submitted_name = request.POST.get('your_name')
            print(f' The name is {submitted_name} and is of type {type(submitted_name)}')
        except exception as e:
            print(e)
        return render(request, "form.html")




