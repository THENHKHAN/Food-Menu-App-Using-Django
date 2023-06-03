from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.template import loader
# relative import of forms
from .models import items # to retrieve the data that are present in model
# Create your views here.
from .forms import itemForm


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
    item = items.objects.get(pk=item_id) # pk is primary key send through router

# If you know there is only one object that matches your query, you can use the   get() method on a Manager which returns the object directly    

    context ={
    "item" : item, # this the above variable i.e. the object whose id is matching.
    }# item will will be passed as an object through context.
#we're going to get only that object whose id is primary key.
    # return HttpResponse(f"This is item no/id {item_id}")
    return render(request, './detail.html' , context)

def create_item(request) :
    form = itemForm (request.POST or None) # creating instance of itemForm class

    # now let's check whether field are valid or not

    if form.is_valid() :
        form.save() # if valid then save the form
        return redirect('food:homePage') # where you wanna redirect after saving the form. 'food:index' === to go to index view/router. index is the function above.
 
    return render(request,'./item_form.html',{"form":form} ) # if form is not valid then render on item_form.html in templates

# updating

def  update_item (request,id) :
    item = items.objects.get(id=id)
    form = itemForm(request.POST or None , instance = item) #instance = item so that field data already present in input box.

    if form.is_valid() :
        form.save()
        return redirect("food:homePage")
    context = {
            "form" : form ,
        }
    return render(request , "./item_form.html " , context)


def delete_item (request,id) :

    item = items.objects.get(id=id)
    if request.method == 'POST':
         item.delete()
         return redirect ('food:homePage' )
   
    return render(request,'./item_delete.html' , {"item":item})