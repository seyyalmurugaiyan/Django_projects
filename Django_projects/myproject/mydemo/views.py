from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    #return HttpResponse("welcome")
    return render(request,"login.html")

def pullrequests(request):
    return HttpResponse("Pull Requests")

def calculate(request):
    x = request.GET['number1']
    y = request.GET['number2']
    z = int(x)+int(y)
    if z%2==0:
        return HttpResponse(f"<h1 style = 'color:green'>Calculation View: {x}+{y}={z}</h1>")
    else:
        return HttpResponse(f"<h1 style = 'color:red'>Calculation View: {x}+{y}={z}</h1>")
