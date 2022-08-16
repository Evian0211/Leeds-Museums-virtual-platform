from cmath import log
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request, *args, **kwargs):
    if request.method == "POST":
        if request.POST.get("logout"):
            logout(request)
            return redirect("/login")
        elif request.POST.get("login"):
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                return render(request, "login.html", {"status": "Authentication failed."})
        elif request.POST.get("register"):
            username = request.POST.get("username")
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")
            if password != confirm_password:
                return render(request, "login.html", {"status": "Password and confirm password is different."})
            else:
                User.objects.create_user(username=username, email="", password=password)
                return render(request, "login.html", {"status": "Register sucessful, please login."})
    return render(request, "login.html", {})

@login_required(login_url="/login")
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

@login_required(login_url="/login")
def account_view(request, *args, **kwargs):
    return render(request, "account.html", {})

@login_required(login_url="/login")
def curriculum_view(request, *args, **kwargs):
    return render(request, "curriculum.html", {})

@login_required(login_url="/login")
def evaluation_view(request, *args, **kwargs):
    return render(request, "evaluation.html", {})

@login_required(login_url="/login")
def evaluation_quiz_view(request, *args, **kwargs):
    return render(request, "evaluation_quiz.html", {})

@login_required(login_url="/login")
def plan_visit_view(request, *args, **kwargs):
    return render(request, "plan_visit.html", {})