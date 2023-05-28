"""
URL configuration for foodProj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/', include("food.urls")), # don't write in 1st arg. And also here don't need to write for every route. Here food.urls means look into app food and in that go in urls.py and look for user request route in views as per the urls given their. We need to write new path only when if we're creating any new app.SO IN GENERAL we use include and app name once. 
    # SINCE i have written here food/ hence browser will look 1st food/ then go into urls.py of app food. ex: food/  --> for home , food/about --> for about etc.
    #  food/about in this did't used slash after about because browser do it itself
]
