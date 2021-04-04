from django import forms

from .models import ChampagneBlogPost


class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = ChampagneBlogPost
        fields = ['title', 'slug', 'content']
