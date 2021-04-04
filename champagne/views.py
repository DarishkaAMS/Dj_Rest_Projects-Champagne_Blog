from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_page_view(request):
    return render(request, "hello.html")


def about_page_view(request):
    return HttpResponse("About us")


def contact_page_view(request):
    return HttpResponse("Contact us")
