from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Post
from .forms import PostForm
# Create your views here.


def index(request):
    return render(request, 'index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'admin.html')

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            messages.success(request, 'Your blog post was successfully created.')
            # return redirect('post_list')
        else:
            messages.error(request, 'There was an error creating your blog post.')
    else:
        form = PostForm()
    return render(request, 'admin.html', {'form': form})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'customer.html', {'posts': posts})


def customer(request):
    return render(request,'customer.html')

def patient_dashboard(request):
    posts = Post.objects.all()
    category = request.GET.get('category')
    if category:
        posts = Post.objects.filter(category=category)
    categories=Post.CATEGORY_CHOICES
    context={'posts':posts,'categories':categories,'selected_category':category}
    return render(request, 'post_by_category.html', context)
