from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    address = models.CharField(max_length=155,  null=True, blank=True)
    class Meta(AbstractUser.Meta):
        swappable  = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Banner(models.Model):
    title = models.CharField(max_length=55)
    desciption = models.CharField(max_length=255)
    img = models.ImageField(upload_to='img_banner/')


class Service(models.Model):
    title = models.CharField(max_length=55)
    desciption = models.CharField(max_length=255)
    img = models.ImageField(upload_to="service_img/")

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    is_sale = models.IntegerField(default=0, null=True, blank=True)
    new_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rating = models.FloatField(default=0)
    soldout = models.BooleanField(null=True, blank=True)
    shopping_policy = models.TextField()
    text = models.TextField()
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE)
    color = models.ForeignKey(to='Color', on_delete=models.CASCADE)
    size = models.ForeignKey(to='Size', on_delete=models.CASCADE)
    material = models.ForeignKey(to='Material', on_delete=models.CASCADE)
    vendoors = models.ForeignKey(to='Vendors', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='Imagge/')
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=55)
    def __str__(self):
        return self.name


class Vendors(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()

class Color(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(to='Block_category', on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateField(auto_now=True)
    description = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='blog_photo')


class Block_category(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name

class Logo(models.Model):
    image = models.ImageField(upload_to='Logo_image/')

class Contact(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    office = models.ForeignKey(to='Office' , on_delete=models.CASCADE)


class Office(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name

class About_company(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to='img_about')

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=55)
    img = models.ImageField(upload_to='img_team')


class Cart(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    product = models.ForeignKey(to='Product', on_delete=models.CASCADE)

class Massage(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=125)
    phone_number = models.CharField(max_length=13, unique=True, null=True, blank=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'

        ), ])
    message = models.TextField()


class Comment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    blog = models.ForeignKey(to=Blog, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)