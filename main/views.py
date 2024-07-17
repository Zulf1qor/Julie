from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, authenticate, logout
def index_view(request):
    context={
        'banner':Banner.objects.all().order_by("-id")[:2],
        'service': Service.objects.all().order_by("-id")[:3],
        'blog':Blog.objects.all().order_by("-id")[:3]
    }
    return render(request, "index.html", context)

def shop_view(request):
    content = {

    }
    return render(request, "shop.html", content)


def wishlist_view(request):
    content = {

    }
    return render(request, "wishlist.html", content)





def cart_view(request):
    content = {

    }
    return render(request, "cart.html", content)


def checkout_view(request):
    content = {

    }
    return render(request, "checkout.html", content)


def product_view(request):
    content = {
        'product':Product.objects.last()
    }
    return render(request, "product.html", content)


def blog_view(request):
    content = {
        'blog':Blog.objects.all().order_by("-id")[:3],

    }
    return render(request, "blog.html", content)


def blog_single_view(request, pk):
    blog = Blog.objects.get(pk=pk)
    content = {
        'blog':blog,


    }
    return render(request, "single-blog.html", content)


def contact_view(request):
    content = {
        'contact':Contact.objects.all().order_by('-id')[:3],
    }
    return render(request, "contact.html", content)

def crete_comment(request):
    if request.method == "POST":
        message = request.POST['message']
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        Massage.objects.create(
            name = name,
            email=email,
            phone_number = phone_number,
            message = message,
        )
        return render(request, "contact.html")


def about_view(request):
    content = {
        'about':About_company.objects.last(),
        'team':Team.objects.all().order_by('-id')[:3]
    }
    return render(request, "about-us.html", content)



def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        User.objects.create_user(
            username = username,
            password = password,
            address = address,
        )
        return redirect("index_url")
    return render(request,'register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request, usr)
        return redirect("index_url")
    return render(request,'login.html')