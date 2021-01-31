from django.http import HttpResponse
from django.shortcuts import render
from . import models
from datetime import datetime
from subprocess import run, PIPE
import sys


# Create your views here.
def index(request):
    return render(request, 'index.html')


def flipkart(request):
    if request.method == "POST":
        url = request.POST['url']
        desired_price = request.POST['cost']
        email = request.POST['mail']
        site = url[12:20]
        if site == 'flipkart':
            a = models.Flipkart(URL=url, Desired_Price=desired_price, Email=email, Time=datetime.now())
            a.save()
        return render(request, 'index.html')
    return render(request, 'flipkart.html')


def amazon(request):
    if request.method == "POST":
        url = request.POST['url']
        desired_price = request.POST['cost']
        email = request.POST['mail']
        site = url[12:18]
        if site == 'amazon':
            a = models.Amazon(URL=url, Desired_Price=desired_price, Email=email, Time=datetime.now())
            a.save()
        return render(request, 'productinfo.html')
    return render(request, 'amazon.html')


def snapdeal(request):
    if request.method == "POST":
        url = request.POST['url']
        desired_price = request.POST['cost']
        email = request.POST['mail']
        site = url[12:20]
        if site == 'snapdeal':
            a = models.Snapdeal(URL=url, Desired_Price=desired_price, Email=email, Time=datetime.now())
            a.save()
        return render(request, 'index.html')
    return render(request, 'snapdeal.html')
