from django.urls import path
from .views import createview,\
    detailview, formview, listview, \
    updateview, func_createview, func_listview,\
     func_detailview, func_updateview, func_deleteview

urlpatterns = [
    #map the url to the welcome function...string urls should be at the top to prevent mismatch.
    path('createview/',createview.as_view()),
    path('listview/',listview.as_view()),
    path('formview/', formview.as_view()),
    path('createviewfunction/', func_createview),
    path('listviewfunction/', func_listview),
    path('search/<id>/', func_detailview),
    path('update/<id>/',func_updateview),
    path('delete/<id>/',func_deleteview),

    #<pk> is identification for id field
    #slug can also be used
    path('<pk>/',detailview.as_view()),
    path('<pk>/update',updateview.as_view()),

    ]