from cmath import log
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request, *args, **kwargs):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login.html", {"status": "Authentication failed."})
    return render(request, "login.html", {})

@login_required(login_url="/login")
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

@login_required
def account_view(request, *args, **kwargs):
    return render(request, "account.html", {})

@login_required
def curriculum_view(request, *args, **kwargs):
    return render(request, "curriculum.html", {})

@login_required
def evaluation_view(request, *args, **kwargs):
    return render(request, "evaluation.html", {})

@login_required
def evaluation_quiz_view(request, *args, **kwargs):
    return render(request, "evaluation_quiz.html", {})

@login_required
def plan_visit_view(request, *args, **kwargs):
    return render(request, "plan_visit.html", {})