from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    print("Request received")  
    return render(request, "app.html")


# Create your views here.
