from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import items # to retrieve the data that are present in model
# Create your views here.


def index (request) :
    lst = items.objects.all()
    # template = loader.get_template('./index.html') No need if using render method
    context = { # whatever data you have obtain from DB , you can send using context to browser/frontend.
    'itemList' : lst,  # 'itemList' will work as a key which store all objects. means equivalent to lst above.
       }

    # return HttpResponse(template.render(context,request)) # working but its better to use render 
    return render(request, './index.html',context)#./index.htlm bcz django knows till templates directory and . means current directory. and ./ means in current directory a file name index.html

    # return HttpResponse("<h1> hello Noor Home </h1>")

def about (request) :
    return HttpResponse("hello Noor it is about")

def listItems (request) :
    lst = items.objects.all() # it will list all the object or item stored in items class
    print(lst)
    return HttpResponse(lst)
    
    
def passVar (request) : # thsi is how to pass variable
    return render(request,"./index.html" , {'first_name': 'Noor', 'last_name': 'KHAN'})


def detail(request,item_id) :
    #  when user click on any item it will direct to this detail URL/route.By id they will be differenctiated.
    # in this we need only that object whose id matched that's y we don't use   items.objects.all() beacuse we  need desire id.
    item = items.objects.get(pk=item_id) # pk is primary key
    print(f"item: {item}")
    context ={

    "item" : item, # this the above variable
    }

    # return HttpResponse(f"This is item no/id {item_id}")
    return render(request, './detail.html' , context)
