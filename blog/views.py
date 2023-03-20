from django.shortcuts import render
from django.views import generic
from .models import Post


class PostDisplay(generic.View):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_date")
    template_name = "blog.html"
    paginate_by = 4
