from cmath import log
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .text import EVALUATION_QUESTIONS, NO_EVALUATION_TEXT
from . import user

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
    evaluation_result = user.get_evaulation_result(request.user)
    if not evaluation_result:
        evaluation_result = NO_EVALUATION_TEXT
    return render(request, "evaluation.html", {"evaluation_result": evaluation_result})

@login_required(login_url="/login")
def evaluation_quiz_view(request, *args, **kwargs):
    if request.method == "POST":
        if request.POST.get("submit"):
            user.update_evaluation_quiz_answer(request.user, request.POST.get("this"), int(request.POST.get("answer")))
            user.evaluate(request.user)
            user.clear_evaluation_answers(request.user)
            return redirect("/evaluation")
        elif request.POST.get("next"):
            user.update_evaluation_quiz_answer(request.user, request.POST.get("this"), int(request.POST.get("answer")))
    if request.GET.get("question"):
        q_number = int(request.GET.get("question"))
    else:
        q_number = 0
    (question_text, choices) = EVALUATION_QUESTIONS[q_number]
    if q_number < len(EVALUATION_QUESTIONS) - 1:
        next = q_number + 1
    else:
        next = -1
    return render(request, "evaluation_quiz.html", {"this": q_number, "next": next, "question": question_text, "choices": choices})

@login_required(login_url="/login")
def plan_visit_view(request, *args, **kwargs):
    return render(request, "plan_visit.html", {})