from django.urls import path
# this dot over here . right before import mean current folder
from . import  views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page") #/posts/my-first-post     => slug is a unique identifier
]