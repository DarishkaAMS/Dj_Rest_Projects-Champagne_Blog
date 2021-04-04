from django.urls import path, re_path

from champagne.views import about_page_view, contact_page_view, example_page_view, home_page_view


urlpatterns = [
    re_path(r'^about/$', about_page_view),
    re_path(r'^pages?/$', about_page_view),
    path('contact/', contact_page_view),
    path('example/', example_page_view),
    path('', home_page_view)
]