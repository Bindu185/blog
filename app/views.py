from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import library
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def index(request):
    books = library.objects.all().values("booktitle","author","author__category","author__gender","publicationid")
    return render(request,"index.html",{"books":books})

def search(request):
    return render(request,"search.html")

def search_action(request):
    search_item=request.GET.get("search_item")
    books=list(library.objects.filter(booktitle__icontains=search_item).values("booktitle","author","author__category","author__gender","publicationid"))
    return JsonResponse({"filtered_results":books})

def signup(request):
    return render(request,"signup.html")

def signin(request):
    return render(request,"signin.html")

def signup_action(request):
    username = request.library.get("email")
    password = request.Post.get("password")
    name =  request.Post.get("name")
    user = User.objects.create_user(username=username,password=password,first_name=name)
    auth.login(request,user)
    return redirect('index')

def signin_action(request):
    username = request.Post.get("email")
    password = request.Post.get("password")
    print(username,password)
    user = auth.authenticate(request,username=username,password=password)
    auth.login(request,user)
    return redirect('index')