from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm

# Create your views here.

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
def profile(request):
    if request.method == "POST":
        form = UserUpdateForm(data= request.POST, instance= request.user)
        if form.is_valid():
            form.save()
            redirect('profile')    
    form = UserUpdateForm(instance=request.user)
    return render(request, template_name="users/profile.html",context= {"form": form})