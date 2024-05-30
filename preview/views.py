from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def index(request):
    template = loader.get_template('html/index.html')
    return HttpResponse(template.render())

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'html/iktree.html', {'post': post})
