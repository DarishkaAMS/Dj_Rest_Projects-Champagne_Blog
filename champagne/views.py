from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template

from .models import ChampagneBlogPost

# Create your views here.


def blog_page_list_view(request):
    queryset = ChampagneBlogPost.objects.all()
    template_name = "blog_page_list.html"
    context = {"object_list": queryset}
    return render(request, template_name, context)


def blog_page_create_view(request):
    template_name = "blog_page_create.html"
    context = {"from": None}
    return render(request, template_name, context)


def blog_page_detail_view(request, slug):
    obj = get_object_or_404(ChampagneBlogPost, slug=slug)
    template_name = "blog_page_detail.html"
    context = {"object": obj}
    return render(request, template_name, context)


def blog_page_update_view(request, slug):
    obj = get_object_or_404(ChampagneBlogPost, slug=slug)
    template_name = "blog_page_update.html"
    context = {"object": obj, "form": None}
    return render(request, template_name, context)


def blog_page_delete_view(request, slug):
    obj = get_object_or_404(ChampagneBlogPost, slug=slug)
    template_name = "blog_page_delete.html"
    context = {"object": obj}
    return render(request, template_name, context)

