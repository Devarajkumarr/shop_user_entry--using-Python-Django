from django.urls import path
from . import views

app_name="flip"

urlpatterns = [
    path("", views.index, name = "index"),
    path("post/detail",views.detail,name="detail"),
    path("post/<int:post_id>/",views.written,name="written"),

    path("old", views.old_url_redirect, name = "old_url"),
    path("new", views.new_url_view, name = "new_url_1"),
                  
]