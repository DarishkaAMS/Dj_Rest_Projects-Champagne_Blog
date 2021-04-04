from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_page_view(request):
    my_title = "Hello there..."
    return render(request, "hello.html", {"title": my_title})


def about_page_view(request):
    return render(request, "about.html", {"title": "About us"})


def contact_page_view(request):
    return render(request, "hello.html", {"title": "Connect us"})
