from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template

from .models import ChampagneBlogPost

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


def example_page_view(request):
    context = {"title": "Example"}
    template_name = "hello.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)


def blog_page_detail_view(request, slug):
    obj = get_object_or_404(ChampagneBlogPost, slug=slug)
    # try:
    #     obj = ChampagneBlogPost.objects.get(id=post_id)
    # except ChampagneBlogPost.DoesNotExist:
    #     raise Http404
    # except ChampagneBlogPost.ValueError:
    #     raise Http404
    template_name = "blog_page_detail.html"
    context = {"object": obj}
    return render(request, template_name, context)
