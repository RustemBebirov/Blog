from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from .models import Category,Blog,Like,Comment,User,About,Contact
from . forms import BlogForm
from django.contrib import messages



def home(request):
    categories = Category.objects.all()
    blogs= Blog.objects.all()  
    ip = request.META.get('REMOTE_ADDR')
    form = BlogForm()
    context = {
        'categories':categories,
        'blogs':blogs,
        'ip':ip,
        'form':form
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

def blog_details(request,pk):
    blog = get_object_or_404(Blog,id=pk)
    comments = Comment.objects.filter(blog_id=blog.id)
    categories = Category.objects.all()
    ip = request.META.get('REMOTE_ADDR')

    if request.method == "POST":
        url = request.META.get('HTTP_REFERER')
        data = request.POST
        user = request.user
        if(user.id):
            comment = Comment.objects.create(
            blog_id= blog.id ,
            user = request.user,
            comment = data['comment']
        )      
            
        return HttpResponseRedirect(url)

    context = {
        'blog':blog,
        'categories':categories,
        'comments':comments,
        'ip':ip
    }
    return render(request, 'details.html',context)


def like_blog(request,pk):
    ip = request.META.get('REMOTE_ADDR')
    url = request.META.get('HTTP_REFERER')
    like = Like.objects.create(
        blog_id=pk,
        isLike=True,
        ip=ip
    )
    messages.success(request, 'Blog successfuy liked')
    return HttpResponseRedirect(url)

def create_blog(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog = form.save()
            blog.save()
            messages.success(request, 'Blog successfuy created')
    return HttpResponseRedirect(url)


def register(request):
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        password = data['password1']
        first_name = data['firstname']
        last_name = data['lastname']
        if (User.objects.filter(username=username)):
            messages.info(request, 'Username already exists')
        else:
            user = User.objects.create(
                username=username,
                first_name = first_name,
                last_name = last_name,
            )
            user.set_password(password)
            user.save()
            return redirect('login')
    return render(request,'register.html')


def login(request):
    if request.method == "POST":
        data = request.POST
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        if user:
            django_login(request,user)
            messages.success(request, 'Login')
            return redirect('blog')
        else:
            messages.warning(request, 'User is not exists')
            return redirect('login')

    return render(request, 'login.html')


def logout(request):
    django_logout(request)
    return redirect('blog')


def about(request):
    about_info = About.objects.filter(id=1).first()
    return render(request,'about.html',{'about_info':about_info})

def contact(request):
    contact_info = Contact.objects.filter(id=1).first()
    return render(request,'contact.html',{'contact_info':contact_info})