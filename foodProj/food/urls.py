

from django.urls import path
from . import views
 
app_name = "food" # for namespacing the url
urlpatterns = [
    #  macthcing url from proj url to app or this app urls to route
    #    /food/
    path('',views.index , name="homePage" ), # home page - route - /food/
    #    /food/about/
    path('about/',views.about , name="about" ), # must to use / after router name.
    #  /food/items/
    path('items/',views.listItems , name="items" ), 
#    /food/passVar/
    path('passVar/',views.passVar , name="passVar" ), 
#  
#   /food/1 or 2 or 3 whatever id you have. The id will come dynamically/by user choic(either by URL box by user or through link). According to that item with of respective id display on detail view 
    path('<int:item_id>',views.detail , name="detail" ), 
    # /food/add/    i.e. add item
    path('add/',views.create_item , name="create_item" ), 
    # edit
    path('update/<int:id>',views.update_item , name="update_item" ),
    # delete 
    path('delete/<int:id>' , views.delete_item , name="delete_item")
]