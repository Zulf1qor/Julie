from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name="index_url"),
    path('shop/', shop_view, name="shop_url"),
    path('wishlist/', wishlist_view, name="wishlist_url"),
    path('login/', login_view, name="login_url"),
    path('cart/', cart_view, name="cart_url"),
    path('checkout/', checkout_view, name="checkout_url"),
    path('product/', product_view, name="product_url"),
    path('blog/', blog_view, name="blog_url"),
    path('blog-single/<int:pk>/', blog_single_view, name="blog-single_url"),
    path('contact/', contact_view, name="contact_url"),
    path('about/', about_view, name="about_url"),
    path('crete_comment/', crete_comment, name="create_comment_url"),
    path('login/', login_view, name="login_url"),
    path('register/', register_view, name="register_url"),


]