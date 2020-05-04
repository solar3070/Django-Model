from django.shortcuts import render
from .models import Blog
# Create your views here.


def home(request):
    paragraphs = Blog.objects
    return render(request, 'home.html', {'blogs' : paragraphs})