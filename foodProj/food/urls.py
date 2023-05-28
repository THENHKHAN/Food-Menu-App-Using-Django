

from django.urls import path
from . import views
urlpatterns = [
    path('',views.index , name="homePage" ), # home page - route - /food/
    path('about/',views.about , name="about" ), # must to use / after router name.
    path('contact/',views.contact , name="contact" ), 
]