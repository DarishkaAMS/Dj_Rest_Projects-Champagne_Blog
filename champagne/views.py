from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_page_view(request):
    return HttpResponse("Good morning beautiful! Welcome Back Home")


def about_page_view(request):
    return HttpResponse("About us")


def contact_page_view(request):
    return HttpResponse("Contact us")
