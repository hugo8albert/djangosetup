from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import Post, Comment, Category


# Create your views here.

def register_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            
        messages.success(request,'Registration successful! Please log in')

        return redirect('login')
    else:
        
        form=UserCreationForm()
        
    return render(request, 'auth/register.html', {'form':form})


def login_view(request):
    
    if request.method=='POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user=form.get_user()
            
            login(request, user)
            
            messages.success(request, 'Logged in successfully!')
            
            return redirect('home')
        else:
            
            form=AuthenticationForm()
            return render(request, 'auth/login.html', {'form':form})
        
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')
        
def home_view(request):
    posts=Post.objects.all().order_by('created_at')
    
    return render(request, 'blog/home.html', {'posts':posts})

#Post detail view
def post_detail_view(request, slug):
    post=get_object_or_404(Post,slug=slug)
    comments=post.comments.all()
    
    if request.method=='POST' and request.user.is_authenticated:
        content=request.POST.get('content')
        
        Comment.objects.create(post=post, author=request.user, content=content)
        
        messages.success(request, 'comment added')
        
        return redirect('post_detail', slug=slug)
    return render(request, 'blog/post_detail.html', {'post':post, 'comments':comments})

#Post view
@login_required

def create_post_view(request):
    if request.method=='POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        category_id=request.POST.get('category')
        slug=title.lower().replace('','-')
        Post.objects.create(
            title=title,
            slug=slug,
            content=content,
            author=request.user,
            category_id=category_id
        )
        
        messages.success(request, 'Post created!')
        return redirect('home')
    categories=Category.objects.all()
    
    return render(request, 'blog/create_post.html',{'categories':categories})


   