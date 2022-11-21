from django.db import models

from Account.models import NewUser


# Do not start Shop_ID at 0, 0 is default.

# User Table(Model)
# class User(models.Model):
#     User_ID = models.PositiveIntegerField(null=False, unique=True)
#     Name = models.CharField(max_length=70, default="", unique=False, null=True)
#     Email = models.EmailField(max_length=254, default="", unique=True)
#     Phone = models.CharField(max_length=12, default="", unique=False, null=True)
#     Username = models.CharField(max_length=70, default="", unique=True)
#     Password = models.CharField(max_length=70, default="", unique=False)
#     Rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
#     IsAdmin = models.BooleanField(null=False, default=False)

# Shop Table(Model)


class Shop(models.Model):
    Shop_ID = models.PositiveIntegerField(null=False, unique=True)
    User_ID = models.OneToOneField(
        NewUser, on_delete=models.CASCADE, parent_link=False)
    Location = models.CharField(max_length=255, default="", unique=False)
    ABN = models.PositiveIntegerField(unique=True, null=True)
    Banner_URL = models.CharField(
        max_length=255, default="", unique=False, null=True, blank=True)
    Logo_URL = models.CharField(
        max_length=255, default="", unique=False, null=True, blank=True)
    Business_Email = models.EmailField(
        max_length=254, default="", unique=False)
    Business_Number = models.CharField(
        max_length=12, default="", unique=False, null=True)
    Business_URL = models.CharField(
        max_length=255, default="", unique=False, null=True, blank=True)
    Description = models.CharField(
        max_length=255, default="", unique=False, null=True, blank=True)
    Business_Name = models.CharField(
        max_length=255, default="", unique=False, null=True, blank=True)


# Address Table


class Address(models.Model):
    User_ID = models.ForeignKey(
        NewUser, on_delete=models.CASCADE, parent_link=False, default=0)
    Address_line1 = models.CharField(max_length=255, default="", unique=False)
    Address_line2 = models.CharField(
        max_length=255, default="", unique=False, null=True)
    City = models.CharField(max_length=70, default="", unique=False)
    Zip = models.PositiveIntegerField(null=False)
    State = models.CharField(max_length=50, default="", unique=False)


# Review Table
class Review(models.Model):
    Rating_ID = models.PositiveIntegerField(null=False, unique=True)
    Reviewer = models.ForeignKey(NewUser, on_delete=models.CASCADE,
                                 parent_link=False, related_name='User_as_Rewiever', default=0)
    Reviewee = models.ForeignKey(NewUser, on_delete=models.CASCADE,
                                 parent_link=False, related_name='User_as_Rewievee', default=0)
    Comment = models.CharField(max_length=255, default="", unique=False)
    Rating_value = models.DecimalField(
        max_digits=3, decimal_places=2, null=False)


# To be determined
# class Categories(models.Model):
#     Category_ID = models.PositiveIntegerField(null=False, unique=True)
#     Category_name = models.CharField(max_length=70, default="",unique=False)
#     Category_type = models.CharField(max_length=70, default="",unique=False)

# Products Table
class Products(models.Model):
    Product_ID = models.PositiveIntegerField(null=False, unique=True)
    Shop_ID = models.ForeignKey(
        Shop, on_delete=models.CASCADE, parent_link=False, default=0)
    # Category_ID = models.OneToOneField(Categories, on_delete=models.CASCADE, parent_link=False)
    Product_name = models.CharField(
        max_length=70, default="", unique=False, null=False)
    Sell_Price = models.DecimalField(
        max_digits=9, decimal_places=2, null=False, default=0.0)
    Rent_Price = models.DecimalField(
        max_digits=9, decimal_places=2, null=False, default=0.0)
    Sponsor_Status = models.BooleanField(null=False, default=False)
    Is_Available = models.BooleanField(null=False, default=True)
    Stock = models.PositiveIntegerField(null=False, unique=False,default=1)


# Media Table
class Media(models.Model):
    Media_ID = models.PositiveIntegerField(null=False, unique=True)
    Storage_location = models.CharField(
        max_length=255, default="", unique=False)
    Product_ID = models.ForeignKey(
        Products, on_delete=models.CASCADE, parent_link=False,  default=0,  unique=False)


# Order Table


class Order(models.Model):
    Order_ID = models.PositiveIntegerField(null=False, unique=True)
    Order_date = models.DateField(auto_now=False, auto_now_add=False)
    Shop_ID = models.ForeignKey(
        Shop, on_delete=models.CASCADE, parent_link=False, default=0)
    Customer_ID = models.ForeignKey(
        NewUser, on_delete=models.CASCADE, parent_link=False, default=0)
    Product_ID = models.ForeignKey(
        Products, on_delete=models.CASCADE, parent_link=False, default=0)
    Amount = models.DecimalField(max_digits=9, decimal_places=2)
    Rent_start = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    Rent_end = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    First_Name = models.CharField(
        null=False, max_length=255, default="", unique=False)
    Last_Name = models.CharField(
        null=False, max_length=255, default="", unique=False)
    Email = models.EmailField(
        null=False, max_length=255, unique=False, default="")
    Phone = models.PositiveIntegerField(null=False, unique=False, default=0)
    Address = models.CharField(
        null=False, max_length=255, default="", unique=False)
    City = models.CharField(null=False, max_length=20,
                            default="", unique=False)
    State = models.CharField(null=False, max_length=4,
                             default="", unique=False)
    ZIP = models.PositiveIntegerField(null=False, unique=False, default=0)


# Product Description
class Product_Description(models.Model):
    Product_ID = models.ForeignKey(
        Products, on_delete=models.CASCADE, parent_link=False, default=0)
    Type = models.CharField(max_length=255, default="",
                            unique=False, null=True, blank=True)
    Age_Range = models.CharField(
        max_length=255, default="", unique=False, null=True, blank=True)
    Brand = models.CharField(max_length=255, default="",
                             unique=False, null=True, blank=True)
    Speeds = models.PositiveIntegerField(null=True, blank=True)
    Colour = models.CharField(
        max_length=255, default="", unique=False, null=True, blank=True)
    Description = models.CharField(
        max_length=255, default="", unique=False, null=True, blank=True)


# Blog
class Blog(models.Model):
    Blog_ID = models.PositiveIntegerField(null=False, unique=True)
    Title = models.CharField(max_length=255, default="", unique=False)
    Preview = models.CharField(max_length=255, default="", unique=False)
    Image_URL = models.CharField(max_length=255, default="", unique=False)
    Blog_URL = models.CharField(max_length=255, default="", unique=False)
    Self_Written = models.BooleanField(null=False, default=False)


class Contact(models.Model):
    Email = models.EmailField(null=False, max_length=255, unique=False)
    First_Name = models.CharField(
        null=False, max_length=255, default="", unique=False)
    Last_Name = models.CharField(
        null=False, max_length=255, default="", unique=False)
    Subject = models.CharField(
        null=False, max_length=255, default="", unique=False)
    Message = models.TextField(
        null=False, max_length=10000, default="", unique=False)


class Cart(models.Model):
    Cart_ID = models.PositiveIntegerField(null=False, unique=True)
    Customer_ID = models.ForeignKey(
        NewUser, on_delete=models.CASCADE, parent_link=False, default=0)
    Product_ID = models.ForeignKey(
        Products, on_delete=models.CASCADE, parent_link=False, default=0)
    # True: buy; False: rent
    Buy_Or_Rent = models.BooleanField(null=False, default=True)
