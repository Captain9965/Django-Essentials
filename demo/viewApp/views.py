
from django.shortcuts import (render,
                            get_object_or_404,
                            HttpResponseRedirect)
from django.http import (HttpResponse)

from django.forms import formset_factory, modelformset_factory
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .forms import vehicleModelForm,AddForm
from .models import vehicleModels
# Create your views here.


""" 
    This is how to declare a class-base view: 
    This is a createview model used to populate the model.

"""
class createview(CreateView):

    """
        every view function takes a request object as its first argument and it is typically named as so
        the view returns a http response object containing the generated response.

    """
    model = vehicleModels
    template_name = 'addData.html'
    fields = ['model', 'engine_capacity']
    success_url = "/listview/"

    # def intro(request):
    #     return HttpResponse("Enjoy the view!")
    # def add_to_db(request):
    #     """ For debugging """
    #     print(request.POST)
    #     context = {}
    #     context['form'] = vehicleModelForm()
    #     return render(request, "addData.html", context)
    # def view_data(request):
    #     context = {}
    #     print(vehicleModels.objects.all())
    #     context['data'] = vehicleModels.objects.all()

    #     """ test data """
    #     # context['data'] = [{"model": "toyota", "engine_capacity": 3500}]
    #     return render(request, "viewData.html", context)

"""
    class-based views: Listview for displaying all the contents

"""
class listview(ListView):
    model = vehicleModels
    template_name = 'viewData.html'

    """
        Make sure you iterate over object list in the view template..
        or else will not work.
    """

    """ 
        override get_query_set() method to get a custom order because the default is to get the objects 
        in the order in which they were created 

        This, for example, gives the object in descending order: 
    
    """
    def get_queryset(self, *args, **kwargs):
        qs = super(listview, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs

"""
    class-based views: Detailview for displaying individual model objects

"""
class detailview(DetailView):
    model = vehicleModels
    template_name = 'viewObject.html'

    """ 
        To override context data or to add some extra fields like so:

    """
    def get_context_data(self, *args, **kwargs):
        context = super(detailview, self).get_context_data(*args, **kwargs)
        context['topic'] = "Vehicles: "
        return context

"""

    class-based views: UpdateView for updating an instance table in a database

"""
class updateview(UpdateView):

    #specify the model and the engine capacity:
    model = vehicleModels
    fields = ['model', 'engine_capacity']
    template_name = 'updateObject.html'

    #This is the url to redirect to afer successful update:
    success_url = "/listview/"


""" class-based views: FormView """

class formview(CreateView):
    form_class = AddForm
    template_name = 'addData.html'
    success_url = '/listview/'

"""
    Function-based views:

        
"""

def func_createview(request):
    context = {}
    form =vehicleModelForm(request.POST or None)
    if form.is_valid():
        print("saving data.......")
        form.save()
    context['form'] = form
    print("running view function..........")
    return render(request, "addData.html", context)


def func_listview(request):
    context = {}
    context['object_list'] = vehicleModels.objects.all()
    return render(request, "viewData.html", context)

#pass id attribute from url:
def func_detailview(request, id):
    context = {}
    context['object'] = get_object_or_404(vehicleModels, id = id)
    return render(request, "viewObject.html", context)

def func_updateview(request, id):
    context = {}
    
    #get the object or return a 404 error:
    obj = get_object_or_404(vehicleModels,id = id)

    #pass the object as instance in form:

    form = vehicleModelForm(request.POST or None, instance=obj)

    #save and redirect when done:
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/search/"+ id)
    context['form'] = form
    return render(request, "updateObject.html", context)
    
def func_deleteview(request, id):
    context = {}

    #get the object or return 404 error:
    obj = get_object_or_404(vehicleModels, id = id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/listviewfunction/")
    return render(request, "deleteObj.html", context)