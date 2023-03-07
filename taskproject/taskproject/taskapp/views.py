from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def demo(request):
    if request.method == 'POST':
        return redirect('login')
    return render(request,"index.html")


# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     ans=x+y
#     return render(request,"result.html",{'result':ans})