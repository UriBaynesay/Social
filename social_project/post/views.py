from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Like
from .forms import PostCreationForm, LikeCreationForm
from django.core.cache import cache

CACH_NAME = 'post_cache'

def home(request):
    if request.method == "POST":
        if post_creations(request):
            return redirect("home")
    form = PostCreationForm()
    if cache.get(CACH_NAME):
       posts = cache.get(CACH_NAME)
    else : 
        posts = Post.objects.all()
        for post in posts:
            post.likes=list(Like.objects.filter(post_id=post.id))
            post.liked = False
            for like in post.likes:
                if request.user and request.user.id == like.user_id.id:
                    post.liked = True
        cache.set(CACH_NAME, posts, 60)
    context = {'posts': posts, 'form': form}
    return render(request, 'post/home.html', context)

@login_required
def _delete_like(request, *args, **kwargs):
    like = Like.objects.get(post_id=kwargs.get('post_id'), user_id=request.user.id)
    like.delete()
    return redirect('home')

def _add_like(request):
    if request.method == "POST":
        form = LikeCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('home')

@login_required
def post_creations(data):
    form = PostCreationForm(data.POST)
    form.instance.author = data.user
    if form.is_valid():
         form.save()
         return True
    return False

def post_details(request,*args, **kwargs):
    post = Post.objects.get(pk= kwargs.get('pk'))
    return render(request= request, template_name= 'post/post-details.html', context= {"post": post})

@login_required
def post_create(request):
    if request.method == "POST":
        if post_creations(request):
            return redirect("home")    
    form = PostCreationForm()
    return render(request= request, template_name= 'post/post-form.html',context={"form": form})

@login_required
def post_update(request,*args, **kwargs):
    post = Post.objects.get(pk= kwargs.get('pk'))
    if post.author != request.user:
        return redirect('home')
    if request.method == "POST":
        form = PostCreationForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostCreationForm(instance= post)
    return render(request= request, template_name='post/post-form.html', context={'form':form})

@login_required
def post_delete(request,*args, **kwargs):
    post = Post.objects.get(pk= kwargs.get('pk'))
    if post.author != request.user:
        return redirect('home')
    else:
        post.delete()
    return render(request= request, template_name='post/post-delete.html')