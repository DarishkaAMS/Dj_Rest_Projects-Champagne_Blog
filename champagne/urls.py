from django.urls import path, re_path

from champagne.views import (blog_page_create_view,
                             blog_page_delete_view,
                             blog_page_detail_view,
                             blog_page_list_view,
                             blog_page_update_view)

urlpatterns = [
    path('', blog_page_list_view),
    path('create/', blog_page_create_view),
    path('<str:slug>/edit/', blog_page_update_view),
    path('<str:slug>/delete/', blog_page_delete_view),
    path('<str:slug>/', blog_page_detail_view),
    # re_pth(r'blog/(?P<slug>\w+)/$', blog_page_detail_view),
    # re_path(r'blog/(?P<post_id>\d+)/$', blog_page_detail_view),

]
