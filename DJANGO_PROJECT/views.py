from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.

# def index(request):
#     return HttpResponse("<h1 style=\"color:blue\">Hello, world!</h1>")

def index(request):
    return render(request, "hello/index.html")

def count(request):
    return render(request, "hello/count.html")

def greet(request):
    return render(request, "hello/greet.html")

def colors(request):
    return render(request, "hello/colors.html")

def select(request):
    return render(request, "hello/select.html")

def tasks(request):
    return render(request, "hello/tasks.html")

def currency(request):
    context = {
        'CURRENCY_ACCESS_KEY': settings.CURRENCY_ACCESS_KEY
    }
    return render(request, "hello/currency.html", context)

# def greet(request, name):
#     return HttpResponse(f"Hello, {name.capitalize()}!")

# def greet(request, name):
#     return render(request, "hello/greet.html", {
#         "name": name.capitalize()
#     })