from django.shortcuts import render,HttpResponseRedirect
from . models import studentform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from . forms import student,signform,loginform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login

def signupuser(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=signform(request.POST)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect("/login/")
        else:
            fm=signform()
        return render(request,"signup.html",{"fm":fm})
    else:
        return HttpResponseRedirect("/home/")

def userlogin(request):
    if request.method=="POST":
        fm=loginform(request=request,data=request.POST)
        if fm.is_valid():
            un=fm.cleaned_data.get("username")
            ps=fm.cleaned_data.get("password")
            user=authenticate(username=un,password=ps)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect("/home/")
    fm=loginform()
    return render(request,"login.html",{"fm":fm})

def userlogout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect("/login/")
    return HttpResponseRedirect("/login/")
  
@login_required     
def homepage(request):
    if request.method=="POST": 
        fm=student(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data.get("name")
            em=fm.cleaned_data.get("email")
            ps=fm.cleaned_data.get("password")
            us=studentform(name=nm,password=ps,email=em)
            us.save()
            return HttpResponseRedirect("/login/")
                
    else:
        fm=student()
    data=studentform.objects.all()
    return render(request,"home.html",{"fm":fm,"data":data})

def update(request,pk):
    if request.user.is_authenticated:
        id=studentform.objects.get(id=pk)
        if request.method=="POST":
            fm=student(data=request.POST,instance=id)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect("/home/")
        fm=student(instance=id)
        return render(request,"update.html",{"fm":fm})
    else:
        return HttpResponseRedirect("/login/")

def deleteuser(request,id):
    if request.user.is_authenticated:
        pk=id
        if request.method=="POST":
            stu=studentform.objects.get(id=pk)
            stu.delete()
            return HttpResponseRedirect("/home/")
    else:
        return HttpResponseRedirect("/login/")