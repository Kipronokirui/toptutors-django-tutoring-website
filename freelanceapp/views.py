from django.shortcuts import render, redirect 
from .models import Post
from .forms import PostForm
from django.utils.text import slugify 
from django.contrib import messages
from .models import Category

# Create your views here.
def index(request):
    posts = Post.objects.all()
    # categorys=Category.objects.all()
    context = {'posts':posts }
    return render(request, "freelanceapp/index.html", context)

def detail(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.exclude(post_id__exact=post.post_id)[:5]
    context = {'post':post,'posts':posts }
    return render(request, "freelanceapp/detail.html", context)

def createPost(request):
    profile = request.user.userprofile 
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.writer = profile 
            post.save()
            messages.info(request, 'Article Succesfully Created')
            return redirect('create')
        else:
            messages.error(request, 'Article Not Created! Try Again Later')
             
    context = {'form':form}
    return render(request, 'freelanceapp/create.html', context)

def updatePost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.info(request, 'Article Succesfully Updated')
            return redirect('detail', slug=post.slug)
        else:
            messages.error(request, 'Article Not Updated! Try Again Later')
    context= {'form':form}
    return render(request, 'freelanceapp/create.html', context)

def deletePost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method == 'POST':
        post.delete()
        messages.info(request, 'Article Succesfully Deleted')
        return redirect('index')
    else:
        messages.error(request, 'Delete Failed! Try Again Later')
    context = {'form': form}
    return render(request, 'freelanceapp/delete.html', context)
