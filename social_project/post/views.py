from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostCreationForm


def home(request):
    if request.method == "POST":
        post_creations(request)
    form = PostCreationForm()
    context = {'posts': Post.objects.all(), 'form': form}
    return render(request, 'post/home.html', context)

@login_required
def post_creations(data):
    form = PostCreationForm(data.POST)
    form.instance.author = data.user
    print(data.user)
    if form.is_valid():
         form.save()
         redirect('/')