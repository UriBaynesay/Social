from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostCreationForm


def home(request):
    if request.method == "POST":
        if post_creations(request):
            return redirect("home")
    form = PostCreationForm()
    context = {'posts': Post.objects.all(), 'form': form}
    return render(request, 'post/home.html', context)

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
