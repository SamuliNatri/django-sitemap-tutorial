from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Post

class PostDetailView(DetailView):

    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
