from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from post.models import Post

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, template_name="users/register.html", context={"form": form})

@login_required
def profile(request, *args, **kwargs):
    if request.method == "POST":
        u_form = UserUpdateForm(data= request.POST, instance= request.user)
        p_form = ProfileUpdateForm(data= request.POST, instance= request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else :
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance= request.user.profile)
        posts = Post.objects.filter(author= request.user)
    return render(request, template_name="users/profile.html",context= {"u_form": u_form, "p_form": p_form, "posts":posts})

@login_required
def delete(request, *args, **kwargs):
    if request.user.id == kwargs.get("pk"):
        user = User.objects.get(id= request.user.id)
        user.delete()
    return render(request, template_name="users/user-delete.html")

