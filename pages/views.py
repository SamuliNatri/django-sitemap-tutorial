from django.shortcuts import render
from django.views.generic.list import ListView
from blog.models import Post

class PostListView(ListView):

    model = Post
    template_name = 'pages/home.html'
    context_object_name = 'posts'