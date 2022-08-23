from cmath import log
import re
from unicodedata import category
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .text import EVALUATION_QUESTIONS, NO_EVALUATION_TEXT, CURRICULUM, RECOMMAND_COURSE, TICKETS
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
    curriculum_status = user.get_curriculum_status(request.user)
    items = user.get_all_items(request.user)
    return render(request, "account.html", {"curriculum_status": curriculum_status, "items": items})


@login_required(login_url="/login")
def curriculum_view(request, *args, **kwargs):
    evaluation = user.get_evaulation_result(request.user)
    if evaluation:
        course_number, course_name, _, _ = RECOMMAND_COURSE[evaluation]
        other_courses = CURRICULUM[:]
        del other_courses[course_number]
    else:
        course_number, course_name = None, None
        other_courses = CURRICULUM
    return render(request, "curriculum.html", {"recommandation": course_name, "course_number": course_number, "other_courses": other_courses})


@login_required(login_url="/login")
def course_view(request, *args, **kwargs):
    if request.GET.get("course"):
        course_number = int(request.GET.get("course"))
        if request.GET.get("section"):
            section_number = int(request.GET.get("section"))
        else:
            section_number = 0
    else:
        return redirect("/curriculum")
    
    _, course_name, course_content, _ = CURRICULUM[course_number]
    category = [header for header, _ in course_content]
    section_header, link = course_content[section_number]
    return render(request, "course.html", {"header": section_header, "link": link, "course_name": course_name, "course_number": course_number, "category": category})


@login_required(login_url="/login")
def course_question_view(request, *args, **kwargs):
    course_number = int(request.GET.get("course"))
    if course_number == None:
        return redirect("/curriculum")
    else:
        if request.method == "POST":
            if request.POST.get("submit"):
                user.update_course_quiz_answer(request.user, course_number, request.POST.get("this"), int(request.POST.get("answer")))
                score = user.mark_course(request.user, course_number)
                user.clear_course_quiz_answers(request.user, course_number)
                user.get_item(request.user, course_number, score)
                # TODO: create a course quiz result page
                return redirect("/")
            elif request.POST.get("next"):
                user.update_course_quiz_answer(request.user, course_number, request.POST.get("this"), int(request.POST.get("answer")))
        if request.GET.get("question"):
            q_number = int(request.GET.get("question"))
        else:
            q_number = 0
        _, _, _, questions = CURRICULUM[course_number]
        (question_text, choices) = questions[q_number]
        if q_number < len(questions) - 1:
            next = q_number + 1
        else:
            next = -1
        return render(request, "course_question.html", {"course_number": course_number, "this": q_number, "next": next, "question": question_text, "choices": choices})


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
    available_to_swap = {}
    unavailable_to_swap = {}
    user_items = user.get_all_items(request.user)
    for ticket, item in TICKETS.items():
        if item in user_items:
            available_to_swap[ticket] = item
        else:
            unavailable_to_swap[ticket] = item

    return render(request, "plan_visit.html", {"available": available_to_swap, "unavailable": unavailable_to_swap})