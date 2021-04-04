from django.urls import path, re_path

from champagne.views import (about_page_view,
                             blog_page_detail_view,
                             blog_page_list_view,
                             contact_page_view,
                             example_page_view,
                             home_page_view)

urlpatterns = [
    path('', home_page_view),
    path('blog/', blog_page_list_view),
    path('blog/<str:slug>/', blog_page_detail_view),
    # re_path(r'blog/(?P<slug>\w+)/$', blog_page_detail_view),
    # re_path(r'blog/(?P<post_id>\d+)/$', blog_page_detail_view),
    path('contact/', contact_page_view),
    path('example/', example_page_view),
    # path('blog/', blog_page_detail_view),
    re_path(r'^about/$', about_page_view),
    re_path(r'^pages?/$', about_page_view),
]
