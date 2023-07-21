from django.shortcuts import render,redirect
from shop.models import Product
from shop.models import Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
# def home(request):
#     p=Product.objects.all()
#     c=Category.objects.all()
#     return render(request,'category.html',{'p':p,'c':c})

def allproducts(request,p):
    c=Category.objects.get(slug=p)
    p=Product.objects.filter(category__slug=p)
    return render(request,"product.html",{'product':p,'c':c})


def allprodcat(request):
    p=Product.objects.all()
    c=Category.objects.all()
    return render(request, "category.html", {'c': c,'p':p})

def prodetail(request,p):
    p=Product.objects.get(slug=p)
    return render(request,'detail.html',{'p':p})

def user_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:allprodcat')
        else:
            messages.error(request, "invalid user")
    return render(request,'login.html')

def register(request):
    if(request.method=="POST"):
        u = request.POST['u']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        p = request.POST['p']
        cp = request.POST['cp']
        if(p==cp):
            u=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            u.save()
            return allprodcat(request)
        else:
            messages.error(request,"PASSWORDS ARE NOT SAME")

    return render(request,'register.html')

@login_required
def user_logout(request):
    logout(request)
    return allprodcat(request)
