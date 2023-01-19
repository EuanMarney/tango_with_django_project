from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! Go to the <a href='http://127.0.0.1:8000/rango/about/'>About</a> page.")

def about(request):
    return HttpResponse("Rango says here is the about page. Go to the <a href='http://127.0.0.1:8000/'>Index</a> page.")
