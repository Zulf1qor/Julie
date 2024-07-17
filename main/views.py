from django.shortcuts import render
from .models import *

def index_view(request):
    context={

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


def login_view(request):
    content = {

    }
    return render(request, "login.html", content)


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

    }
    return render(request, "product.html", content)


def blog_view(request):
    content = {

    }
    return render(request, "blog.html", content)


def blog_single_view(request):
    content = {

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