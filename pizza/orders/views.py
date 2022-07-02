from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.shortcuts import redirect, render


def index(request):
    if request.user.is_authenticated:                   #checking if user login
        times=Cart.objects.filter(user_id=request.user.id)
        if times is not None:
            for time in times:
                food=time.food.all()
                for food in food:
                    food=food
            context={
                "foods":Food.objects.all(),
                "user":request.user,
                # "times":time
            }
            return render(request,"index.html",context)
        return render(request,"index.html")
    return redirect("login")

def login(request):
    if request.user.is_authenticated:                #checking if user login
        return redirect("/")                         #redirecting to index page if user login
    elif request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)     #checking user info correct
        if user is not None:
            auth.login(request,user)                                    #login
            return redirect("/")
        else:
            messages.error(request,"Crendentials Invalid!")
            return redirect("login")

    return render(request,"login.html")

def register(request):
    if request.user.is_authenticated: #checking user login
        return redirect("/")
    elif request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        password=request.POST["password"]
        password0=request.POST["password0"]
        if password != password0:
            messages.error(request,"ERROR!, Password Does Not Match")
            return render(request,"register.html")
        user=User.objects.create(username=username,email=email,first_name=fname,last_name=lname)#saving userinfomation
        User.set_password(user,password)
        user.save()
        addToCart=Cart(user_id=user.id,username=user.username)
        addToCart.save()
        return redirect("login")
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect("login")
    
def cart(request):
    if not request.user.is_authenticated: #checking user login
        return redirect("login")
    if request.method=="POST":
        food_id=request.POST["food_id"]  #Getting food data where the user clicks
        user=request.user
        food=Food.objects.filter(id=food_id).first()
        addToCart=Cart.objects.filter(user_id=user.id).first()
        addToCart.food.add(food)
        times=Times.objects.filter(user_id=user.id,food_id=food_id).first()
        if times:
            times.times+=1
            times.save()
        else:
            createTimes=Times(user_id=user.id,food_id=food_id,times=1)
            createTimes.save()
        return redirect("/")
    
def saveItem(request):
    if not request.user.is_authenticated: #checking user login
        return redirect("login")
    foods=Cart.objects.filter(user_id=request.user.id).all()
    for food in foods:
        food=food.food.all()
    return render(request,"saveItem.html",{"foods":food})
        
def removeItem(request):
    if not request.user.is_authenticated: #checking user login
        return redirect("login")
    if request.method=="POST":
        food_id=request.POST["food_id"]
        food=Food.objects.filter(id=food_id).first()
        removeFromCart=Cart.objects.filter(user_id=request.user.id)
        times=Times.objects.filter(user_id=request.user.id,food_id=food_id).first()
        if times:
            times.times -= 1
            times.save()
        ###|||||###
        if times.times==0:
            for i in removeFromCart:
                i.food.remove(food)
                times.save()
        elif times.times<0:
            times.times=0
            times.save()
            for i in removeFromCart:
                i.food.remove(food)
                times.save()
    return HttpResponseRedirect(reverse("shopping"))

def sendJson(request):
    times=Times.objects.filter(user_id=request.user.id).all()
    data=[]
    for time in times:
        temp=[time.user_id,time.food_id,time.times]
        data.append(temp)
    return JsonResponse(data,safe=False)

