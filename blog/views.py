from django.shortcuts import render
from .models import Post
import datetime


def index(request):
    week_ago = datetime.date.today() - datetime.timedelta(days=7)
    trends = Post.objects.filter(time_upload__gte=week_ago).order_by('-read')

    parms = {
        'posts': Post.objects.filter(published=True),
        'trends': trends[:4],
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
