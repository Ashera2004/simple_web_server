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
from django.http import HttpResponse

def home(request):
    print("Request received")  
    return render(request, "app.html")

app.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Colorful Webpage</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
            background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fad0c4, #ffdde1);
            color: white;
        }
        h1 {
            font-size: 48px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }
        p {
            font-size: 20px;
        }
        .color-box {
            width: 300px;
            height: 300px;
            background: radial-gradient(circle, #ff758c, #ff7eb3);
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            margin: 20px auto;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
            font-size: 24px;
            font-weight: bold;
            color: white;
        }
        .info {
            margin-top: 20px;
            font-size: 22px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Colorful Webpage</h1>
    <p>Enjoy the vibrant gradient background and dynamic visuals!</p>
    <div class="color-box">
        Colorful Box
    </div>
    <div class="info">
        <p>Name: A S Siddarth</p>
        <p>Reg No: 212224040316</p>
    </div>
</body>
</html>


```
# OUTPUT:

![alt text](<Screenshot 2025-04-02 122126.png>)


![alt text](<Screenshot 2025-03-25 160656.png>)

# RESULT:
The program for implementing simple webserver is executed successfully.
