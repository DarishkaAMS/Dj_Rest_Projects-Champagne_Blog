from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template

from .forms import BlogPostForm, BlogPostModelForm
from .models import ChampagneBlogPost

# Create your views here.


def blog_page_list_view(request):
    queryset = ChampagneBlogPost.objects.all()
    template_name = "champagne/blog_page_list.html"
    context = {"object_list": queryset}
    return render(request, template_name, context)


@staff_member_required
# @login_required
def blog_page_create_view(request):
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        # obj = ChampagneBlogPost.objects.create(**form.cleaned_data)
        obj = form.save(commit=False)
        obj.user = request.user
        # obj.title = form.cleaned_data.get("title") + " :)"
        obj.save()
        form = BlogPostModelForm()
    template_name = "form.html"
    context = {"form": form}
    return render(request, template_name, context)


def blog_page_detail_view(request, slug):
    obj = get_object_or_404(ChampagneBlogPost, slug=slug)
    template_name = "champagne/blog_page_detail.html"
    context = {"object": obj}
    return render(request, template_name, context)


def blog_page_update_view(request, slug):
    obj = get_object_or_404(ChampagneBlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = "form.html"
    context = {"form": form, "tile": f"Update {obj.title}"}
    return render(request, template_name, context)


def blog_page_delete_view(request, slug):
    obj = get_object_or_404(ChampagneBlogPost, slug=slug)
    template_name = "champagne/blog_page_delete.html"
    context = {"object": obj}
    return render(request, template_name, context)

