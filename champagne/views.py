from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

# Create your views here.


def home_page_view(request):
    my_title = "Hello there..."
    context = {"title": my_title}
    return render(request, "home.html", context)


def about_page_view(request):
    return render(request, "about.html", {"title": "About us"})


def contact_page_view(request):
    return render(request, "hello.html", {"title": "Connect us"})


def example_page_view(request):
    context = {"title": "Example"}
    template_name = "hello.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)
