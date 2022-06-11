from django.shortcuts import redirect
from django.urls import path
from django.views import View
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
   # path('', views.index),

    path('', views.root),
    path("blogs", views.index),
    path("blogs/new/",views.new),
    path("blogs/create/",views.create),
    path("blogs/<int:number>",views.show),
    path("blogs/<int:number>/edit",views.edit),
    path("blogs/<int:number>/delete",views.delete),
    path("blogs/json",views.json),
 





]

