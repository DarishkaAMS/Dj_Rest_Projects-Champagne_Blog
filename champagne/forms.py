from django import forms

from .models import ChampagneBlogPost


class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = ChampagneBlogPost
        fields = ['title', 'slug', 'content', 'image', 'publish_date']

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        print(instance)
        title = self.cleaned_data.get('title')
        qs = ChampagneBlogPost.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)  # id=instance.id
        if qs.exists():
            raise forms.ValidationError("This title has already been used")
        return title
