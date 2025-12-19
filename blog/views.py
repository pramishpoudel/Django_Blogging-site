from django.shortcuts import render
from .models import Category,Blog

# Create your views here.
def home_blogs(request):
    categories = Category.objects.all()
    featured_blogs = Blog.objects.filter(is_featured=True).order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False,status='Publish')
    context={ 
            'categories': categories,
            'featured_blogs': featured_blogs,
            'posts': posts,
             }
    return render(request, 'home-blogs.html',context)


