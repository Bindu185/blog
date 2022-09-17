from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Library
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def index(request):
    books=Library.objects.all().values("booktitle","bookid","is_available","author__name","author__email","author__gender","image")
    return render(request,"index.html",{"books":books})

def search(request):
    return render(request,"search.html")

def search_action (request):
    search_item =request.GET.get("search_item")
    books=list(Library.objects.filter(author__name__icontains=search_item).values("booktitle","bookid",
    "is_available",
    "author__name","author__email","author__gender"))
    return JsonResponse({"filtered_results":books})
    

def signup(request):
    return render(request,"signup.html")

def signin(request):
    return render(request,"signin.html")
#@csrf_exempt
def signup_action(request):
    username=request.POST.get("email")
    password=request.POST.get("password")
    name=request.POST.get("name")
    user=User.objects.create_user(username=username,password=password,first_name=name)
    auth.login(request,user)
    return redirect('index')

def signin_action(request):
    username=request.POST.get("email")
    password=request.POST.get("password")
    print(username,password)
    user=auth.authenticate(request,username=username,password=password)
    auth.login(request,user)
    return redirect('index')