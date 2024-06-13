from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import BlogPost


# def index(request):
#     blog_posts = BlogPost.objects.all()
#     return render(request, 'html/index.html', {'blog_posts': blog_posts})



def blog_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'html/iktree.html', {'blog_posts': blog_posts})





def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'html/iktree.html', {'post': post})





# views.py
from django.http import JsonResponse
from django.shortcuts import render
from .forms import NewsletterSubscriptionForm

from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from .forms import NewsletterSubscriptionForm

def index(request):
    blog_posts = BlogPost.objects.all()
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return render(request, 'html/index.html', {'form': form, 'error_message': 'Bu e-posta adresi zaten mevcut. Lütfen başka bir adres deneyin.', 'blog_posts': blog_posts})
    else:
        form = NewsletterSubscriptionForm()
    return render(request, 'html/index.html', {'form': form, 'blog_posts': blog_posts})


