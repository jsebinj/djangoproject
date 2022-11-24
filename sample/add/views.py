from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'form.html')


def add(request):
    num1=request.GET["num1"]
    num2=request.GET["num2"]
    res=num1+num2
    return render(request,'result.html',{"result":res})
