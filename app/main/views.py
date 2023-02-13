from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,'main/index.html')


def about(request):
    return render(request,'main/about.html')


def our_objects(request):
    return render(request,'main/our objects.html')


def price(request):
    return render(request,'main/price.html')
