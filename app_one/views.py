from multiprocessing import context
import re
from django import http
from django.shortcuts import redirect, render, HttpResponse
from django.http import JsonResponse

# Create your views here.
def root(request):
    return redirect("/blogs")   #/ - redirects to the "/blogs" route with a method called "root"
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")  #/blogs - display the string "placeholder to later display a list of all blogs" with a method named "index"
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog") #/blogs/new - display the string "placeholder to display a new form to create a new blog" with a method named "new"
def create(request):
    return redirect('/') #/blogs/create - redirect to the "/" route with a method called "create"


def show(request,number):#/blogs/< number > - display the string "placeholder to display blog number: {number}" with a method named "show" (eg. localhost:8000/blogs/15 should display the message: 'placeholder to display blog number 15')
   number = f"placeholder to display blog {number}"
   return HttpResponse(number)

    #/blogs/< number >/edit - display the string "placeholder to edit blog {number}" with a method named "edit"
def edit(request,number):
   number = f"placeholder to edit blog {number}"
   return HttpResponse(number)
#/blogs/< number >/delete - redirect to the "/blogs" route with a method called "destroy"
def delete(request,number):
   number= "Delete article Number : %s" %number
   return redirect("/blogs")


#(**Bonus**) /blogs/json - return a JsonResponse with title and content keys.
def json(request):
    return JsonResponse({
        'title':'my first blog',
       ' content_key':'ljgsadoiuqwefgo  qiuewgd pqiwugdbiuwqgdvb '

    })







