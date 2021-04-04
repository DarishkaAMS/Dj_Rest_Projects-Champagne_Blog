from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template

# Create your views here.


def home_page_view(request):
    my_title = "Hello there..."
    context = {"title": "not Authenticated"}
    if request.user.is_authenticated:
        context = {"title": my_title, "my_list": [1, 2, 3, 4, 5]}
    return render(request, "home.html", context)


def about_page_view(request):
    return render(request, "about.html", {"title": "About us"})


def contact_page_view(request):
    return render(request, "hello.html", {"title": "Connect us"})

