from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ProjectCentricMail.forms import SignUpForm
from ProjectCentricMail.caller import gmail_read
from ProjectCentricMail.auto import run
from ProjectCentricMail.merge import mer
from ProjectCentricMail.models import MessageInfo,ProjectClassify,ProjectNames
from ProjectCentricMail.sort import read
from ProjectCentricMail.formalinformal import PCM_formalinformal
import csv
import os
import threading
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "ProjectCentricMail/login.html", {"message": None})
    context = {
        "user": request.user
    }
    r = User.objects.get(username=request.user)
    print(r.email)
    processThread = threading.Thread(target=gmail_read, args=[request.user])  # <- 1 element list
    processThread.start()
    print(request.user)
    return render(request, "ProjectCentricMail/user.html", context)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'ProjectCentricMail/signup.html', {'form': form})
    
def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        processThread = threading.Thread(target=gmail_read, args=[request.user])  # <- 1 element list
        processThread.start()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "ProjectCentricMail/login.html", {"message": "Invalid credentials." , "notetype":"danger"})

def logout_view(request):
    logout(request)
    return render(request, "ProjectCentricMail/login.html", {"message": "Logged out." , "notetype":"info"})

def spam_view(request):
    if not request.user.is_authenticated:
        return render(request, "ProjectCentricMail/login.html", {"message": None})
    username=request.user
    processThread = threading.Thread(target=gmail_read, args=[request.user])  # <- 1 element list
    processThread.start()
    run(username)
    mer(username)
    print(request.user)
    module_dir = os.path.dirname(__file__)
    f = open(os.path.join(module_dir,f'csvfile/{username}_final.csv'))
    reader = csv.reader(f)
    r = User.objects.get(username=request.user)
    context = {
        "user": request.user ,
        "reader":reader , 
        "email":r.email
    }
    return render(request, "ProjectCentricMail/mails.html", context)

def project_view(request):
    if not request.user.is_authenticated:
        return render(request, "ProjectCentricMail/login.html", {"message": None})
    if request.method == 'POST':
    	projectname = request.POST["projectname"]
    	count = ProjectNames.objects.filter(username=request.user,projectname=projectname).count()
    	if count == 0 :
    		tuplep = ProjectNames(username=request.user,projectname=projectname)
    		tuplep.save()
    projectname = ProjectNames.objects.filter(username=request.user)	    
    context = {
        "user": request.user ,
        "projectname":projectname , 
    }
    return render(request, "ProjectCentricMail/projectnames.html", context)

def projectsort_view(request,projectname):
    if not request.user.is_authenticated:
        return render(request, "ProjectCentricMail/login.html", {"message": None})
    projects = ProjectNames.objects.filter(username=request.user)
    processThread = threading.Thread(target=gmail_read, args=[request.user])  # <- 1 element list
    processThread.start()
    listp=[]
    n=ProjectNames.objects.filter(username=request.user).count()
    for i in projects:
    	listp.append(i.projectname)
    read(request.user,listp,n)
    module_dir = os.path.dirname(__file__)
    f = open(os.path.join(module_dir,f'csvfile/{request.user}_finalproject.csv'))
    reader = csv.reader(f)
    r = User.objects.get(username=request.user)
    context = {
        "user": request.user,
        "reader":reader,
        "projectname":projectname, 
        "email":r.email
    }
    return render(request, "ProjectCentricMail/project.html", context)

def formalinformal_view(request):
    if not request.user.is_authenticated:
        return render(request, "ProjectCentricMail/login.html", {"message": None})
    processThread = threading.Thread(target=gmail_read, args=[request.user])  # <- 1 element list
    processThread.start()
    PCM_formalinformal(request.user)
    module_dir = os.path.dirname(__file__)
    f = open(os.path.join(module_dir,f'csvfile/{request.user}_finalformal.csv'))
    reader = csv.reader(f)
    r = User.objects.get(username=request.user)
    context = {
        "user": request.user,
        "reader":reader, 
        "email":r.email
    }
    return render(request, "ProjectCentricMail/formalinformal.html", context)
    
def about_view(request):
    if not request.user.is_authenticated:
        return render(request, "ProjectCentricMail/login.html", {"message": None})
    context = {
        "user": request.user
    }
    r = User.objects.get(username=request.user)
    print(r.email)
    processThread = threading.Thread(target=gmail_read, args=[request.user])  # <- 1 element list
    processThread.start()
    print(request.user)
    return render(request, "ProjectCentricMail/about.html", context)


def del_user(request):    
    try:
        username = request.user
        u = User.objects.get(username = username)
        u.delete()
        render(request, 'ProjectCentricMail/login.html',{"message":"Account Deleted","notetype":"info"})           

    except User.DoesNotExist:
        messages.error(request, "User doesnot exist")    
        return render(request, 'ProjectCentricMail/login.html')

    except Exception as e: 
        return render(request, 'ProjectCentricMail/login.html',{"message":e.message,"notetype":"info"})

    return render(request, 'ProjectCentricMail/login.html',{"message":"Account Deleted","notetype":"info"})
