from ast import Try
from email.mime import image
from pickle import TRUE
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver 
from django.db.models.signals import post_save
# adding new imports
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
# Class customer is created to extend the User model
# Attributes user are inherited by the User model
# Contain the name and email of the user
# custom imports
from django.shortcuts import render, redirect
from django.contrib import messages
# from .models import Product

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True,blank=True, related_name = "customer")
    name=models.CharField(max_length=200,null=True)    
    email=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

# Class Product is created to store the products
# Attributes name, price, slug, category, digital, image, stock and stock_limit
# Method imageURL is to get the image of the product
class Product(models.Model):
    name=models.CharField(max_length=200,null=True)   
    price=models.DecimalField(max_digits=7,decimal_places=2,validators=[MinValueValidator(0.01)]) 
    slug=models.SlugField(max_length=200,default="")
    category=models.CharField(max_length=200,null=True) 
    digital=models.BooleanField(default=False,null=True,blank=True)
    image= models.ImageField(null=True,blank=True)
    stock = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    stock_limit = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1)])

    def save(self, *args, **kwargs):
        if self.stock >= self.stock_limit:
            raise ValidationError("Stock must be lower than stock limit")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except: 
            url=''
        return url


# Class Order is created to store the orders
# Attributes customer, date_ordered, complete, transaction_id
# Metods get_cart_total, get_cart_items and shipping are to get the total, the items and the shipping of the order
class Order(models.Model):
    #a single customer can have multiple orders
    customer = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    order_day = models.DateField(auto_now_add=True, null= True)
    complete=models.BooleanField(default=False,null=True,blank=False)
    transaction_id=models.CharField(max_length=100,null=True)  
    total_money = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        if self.customer is not None:
            return str(self.customer)
        return "Unknown"
   

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        self.total_money = total
        self.save()
        return total
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    @property
    def shipping(self):
        shipping=False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping=True
            return shipping
        
    def save(self, *args, **kwargs):
     if self.complete:
        order_items = self.orderitem_set.all()
        for item in order_items:
            if item.product is not None:
                #item.product.stock -= item.quantity
                item.product.save()
     super().save(*args, **kwargs)



# Class OrderItem is created to detailed the order
# Attributes product, order, quantity and date_added
# Metod get_total is to get the total of the order
class OrderItem (models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True, validators=[MinValueValidator(0)])
    date_added = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        if self.product is not None:
            total = self.product.price * self.quantity
            return total
        return 0
    
    def save(self, *args, **kwargs):
        if self.product is not None:
            if self.product.stock - self.quantity < 0:
                raise ValidationError("quantity must lower than stock")
            self.product.save()
        super().save(*args, **kwargs)



# Class ShippingAddress is created to store the shipping address
# Attributes customer, order, name, address, city, state, zipcode and date_added
class ShippingAddress (models.Model):
    customer = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True, related_name='addresse')
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=200,null=True)   
    address=models.CharField(max_length=200,null=True)   
    city=models.CharField(max_length=200,null=True)   
    state=models.CharField(max_length=200,null=True)   
    zipcode=models.CharField(max_length=200,null=True)   
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


# Class post use to store the post in the blog
# Attributes title, description, slug, date_posted and image
class Post(models.Model):
    title=models.CharField(max_length=200,null=True)   
    description=models.CharField(max_length=800,null=True) 
    slug=models.SlugField(max_length=200,default="")   
    date_posted = models.DateTimeField(auto_now_add=True)
    image= models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.title
        
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except: 
            url=''
        return url


# Class Comment is created to store the comments in the blog
# Attributes post, name, body and date_commented
class Comment(models.Model):
    post=models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    body=models.TextField(max_length=200)
    date_commented=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)


# Func create_user_customer is created to create a customer when a user is created
# It is called when a user is created and create an instance of customer
@receiver(post_save, sender=User)
def create_user_customer(sender, instance, created, **kwargs):
	print('****', created)
	if instance.is_staff == False:
		Customer.objects.get_or_create(user = instance, name = instance.username, email = instance.email)
