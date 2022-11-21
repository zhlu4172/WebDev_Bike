from django.contrib import admin

from .models import Blog, Product_Description, Shop, Address, Order, Media, Review, Products, Contact, Cart

admin.site.register(Shop)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(Media)
admin.site.register(Review)
admin.site.register(Products)
admin.site.register(Product_Description)
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(Cart)
