# EX01 Developing a Simple Webserver

# Date: 24/03/2025
# AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

# DESIGN STEPS:
## Step 1:
HTML content creation.

## Step 2:
Design of webserver workflow.pus

## Step 3:
Implementation using Python code.

## Step 4:
Serving the HTML pages.

## Step 5:
Testing the webserver.

# PROGRAM:
```
urls.py

from django.contrib import admin
from django.urls import path
from web_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home)
]



views.py

from django.shortcuts import render
def home(request):
    return render(request,"app.html")


```
# OUTPUT:

![alt text](<Screenshot 2025-03-25 154755.png>)

# RESULT:
The program for implementing simple webserver is executed successfully.
