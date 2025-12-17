from django.shortcuts import render


# Create your views here.
def home_blogs(request):
    return render(request, 'home-blogs.html')