from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index (request) :
    return HttpResponse("<h1> hello Noor Home </h1>")

def about (request) :
    return HttpResponse("hello Noor it is about")

def contact (request) :
    return HttpResponse("hello Noor it is contact")