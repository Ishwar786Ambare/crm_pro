from django.shortcuts import render
from .models import Post


# Create your views here.
def index(request):
    parms = {
        'posts': Post.objects.filter(published=True)
    }
    return render(request, 'index.html', parms)


def about(request):
    parms = {
        'title': 'About | NextClick',
    }
    return render(request, 'about.html', parms)


def categories(request):
    return render(request, 'categories.html')


def post(request):
    return render(request, 'blog-single.html')


def contact(request):
    return render(request, 'contact.html')
