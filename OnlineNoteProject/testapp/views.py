from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from testapp.models import Topic
def start_view(request):
    return render(request,'testapp/start.html')

def signUp_view(request):
    if request.method=='POST':
           username=request.POST.get('username')
           password=request.POST.get('password')
           cpasswor=request.POST.get('rpassword')
           User.objects.create_user(username=username,password=password)
           return redirect('login')
    return render(request,'testapp/signup.html')

def login_view(request):
    if request.method=='POST':
         username=request.POST.get('username')
         password=request.POST.get('password')
         user =authenticate(request,username=username,password=password)
         if user is not None:
              login(request,user)
              return redirect('home')
    return render(request,'testapp/login.html')
def logout_view(request):
     logout(request)
     return redirect('login')

@login_required(login_url='login')
def home_view(request):
    return render(request,'testapp/home.html')



def add_topic_view(request):
     if request.method=='POST':
          topic=request.POST.get('topic')
          subject=request.POST.get('subject')
          Topic.objects.get_or_create(topic=topic,subject=subject)
          return redirect('/home')
     return render(request,'testapp/addtopic.html')


def show_topic_view(request):
     user=Topic.objects.all()
     return render(request,'testapp/showtopic.html',{"user":user})
