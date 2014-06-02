from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.utils.functional import lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
import random

from .forms import AccountCreateForm, AccountAuthForm
from core.views import index
from utils.func import *

reverse_lazy = lambda name=None, *args: lazy(reverse, str)(name, args=args)


########################
# View profile
########################

@login_required
def view_profile(request): #, search_query=""):
    #form = EventForm(data=request.POST or None, user=request.user)
    template = 'account/view_profile.html'

    try:
        user_id = request.GET.get('user_id','')
        student = Account.objects.get(user__username=user_id)
    except:
        student = None
        pass

    return render(request,
                  template,
                  {'student' : student,})


########################
# Follow friends
########################

@login_required
def follow(request):
    if request.method == 'POST':
        username = request.POST.get("username", "")
        student = get_student_from_usernme(username)

        current_student = get_student_from_user(request.user) 

        if student in current_student.friends.all():
          current_student.friends.remove(student)
        else:            
          current_student.friends.add(student)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

########################
# Sign in (Log in)
########################

def sign_in(request):
    form = AccountAuthForm(data = request.POST or None)
    template = 'account/sign_in.html'

    next_url = request.POST.get("next", "/")

    if request.method == 'POST':
        if form.is_valid():
            print "1!23"
            print form.get_user()
            login(request, form.get_user())

            return redirect(next_url)
        else:
            print "2!23"
            return render(request, template, {'form': form, 'nav_bar': True, 'next': next_url, })

    return render(request, template, {'form': form, 'nav_bar': True, 'next': next_url, })

########################
# Sign up (Join)
########################

def sign_up(request):
    form = AccountCreateForm(data = request.POST or None)
    template = 'account/sign_up.html'

    if request.method == 'POST':
        if form.is_valid():
            username = form.clean_username()
            password = form.clean_password2()
            new_user = form.save()
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect("/")
        else:
            return render(request, template, {'form': form, 'nav_bar': True,})

    return render(request, template,  {'form': form,  'nav_bar': True,})

########################
# Sign out (Log out)
########################

@login_required
def sign_out(request):
    logout(request)

    return redirect('/')
