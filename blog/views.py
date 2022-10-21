from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import login as django_login, logout as django_logout, authenticate, get_user_model
from .models import Category,Blog,Like

def home(request):
    categories = Category.objects.all()
    blogs= Blog.objects.all()  
    ip = request.META.get('REMOTE_ADDR')
    for category in categories:
        print(category.parent)
    context = {
        'categories':categories,
        'blogs':blogs,
        'ip':ip
    }
    return render(request, 'index.html',context)

def category(request,slug):
    categories = Category.objects.all()
    blogs = Blog.objects.filter(category__slug=slug)
    ip = request.META.get('REMOTE_ADDR')

    context = {
        'categories':categories,
        'blogs':blogs,
        'ip':ip
    }

    return render(request, 'category.html',context)

def like_blog(request,pk):
    ip = request.META.get('REMOTE_ADDR')
    url = request.META.get('HTTP_REFERER')
    like = Like.objects.create(
        blog_id=pk,
        isLike=True,
        ip=ip
    )
    return HttpResponseRedirect(url)




def login(request):
    if request.method == "POST":
        print('ela')

    return render(request, 'login.html')


def logout(request):
    django_logout(request)
    return redirect('blog')