from pyexpat import model
from django.http import HttpResponse
from django.shortcuts import (render, HttpResponseRedirect, get_object_or_404)
from .models import vehicleModels as v

# Create your views here.

def createModel(request):
    try:
        if (request.method == "POST" and request.POST.get('model') and request.POST.get('engine_capacity')):
            print(type(request.POST.get('model')))
            obj = v(
                model = request.POST.get('model'),
                engine_capacity = request.POST.get('engine_capacity')
            )
            obj.save()
            print("objects saved..")
            return HttpResponseRedirect("/model/listobjects/")
    except Exception as e:
        print(e)   
    context = {}
    return render(request, "createModel.html", context)

def listObjects(request):  
    try:
        objects = v.objects.all();
    except Exception as e:
        print(e)
        return HttpResponseRedirect("/model/createmodel/")

    context = {}
    context['object_list'] = objects if objects is not None else None
    response = HttpResponse(render(request, "viewModel.html", context))

    """ testing session cookies: """

    response.set_cookie('visits',int(request.COOKIES.get('visits', 1)) +1)
    print("visits-> %d"%int(request.COOKIES.get('visits',1)))

    """ end of cookies test """
    return response

def updateModel(request, id):
    context = {}
    if(v.objects.get(id = id) is not None):
        context['model'] = v.objects.get(id = id).model
        context['engine_capacity'] = v.objects.get(id = id).engine_capacity
    try:
        if(request.method == "POST"):
            model = request.POST.get('model')
            engine_capacity = request.POST.get('engine_capacity')
            if (model):
                obj = v.objects.get(id = id)
                if obj is not None:
                    obj.model = model
                    obj.save()
                else:
                    return HttpResponse("Model not found")
            if(engine_capacity):
                obj = v.objects.get(id = id)
                if obj is not None:
                    obj.engine_capacity = engine_capacity
                    obj.save()
                else:
                    return HttpResponse("Model not found")
            return HttpResponseRedirect("/model/listobjects/")
    except Exception as e:
        print(e)
        return HttpResponse("Error occured, contact Admin")
    return render(request, "updateModel.html", context)

def slugView(request, slug):
    print(slug)
    object = v.objects.filter(slug__iexact = slug)
    if object.exists():
        object = object.first()
    else:
        return HttpResponse('<h1> vehicle model not found </h1>')
    context = {
        'object': object
    }
    return render(request, "showObject.html",context)


