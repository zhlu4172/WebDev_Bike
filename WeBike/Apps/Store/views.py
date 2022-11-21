from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from .models import Review, Media, Products, Blog, Product_Description, Shop, Cart, Order

from .models import Review, Media, Products, Blog, Contact, Product_Description, Shop
from django.conf import settings
from django.core.mail import send_mail

from django.http import HttpResponse, JsonResponse
from django.conf import settings
import stripe

# Create your views here.


def home(request):
    # Get reviews
    # Maybe have 3 random reviews?
    review = Review.objects.all()
    product = Products.objects.all()
    media = Media.objects.all()
    product_media = Media.objects.all().select_related("Product_ID")


    context = {
        "reviews": review,
        "products": product,
        "medias": media,
        "product_media": product_media,
    }
    return render(request, 'Store/homepage.html', context)


def about_us(request):
    return render(request, 'Store/AboutUsPage.html')


def cart_page(request):
    return render(request, 'Store/CartPageTemplate.html')


def contact_us(request):
    return render(request, 'Store/ContactUs.html')


@login_required
def paymentpage(request):
    cart = Cart.objects.all().filter(Customer_ID=request.user)
    media = Media.objects.all()
    context = {
        "cart": cart,
        "media": media,
    }
    if request.method == 'POST':
        for product in cart:
            if product.Product_ID.Stock <= 0:
                break
            new_id = 1
            while True:
                if Order.objects.filter(Order_ID=new_id).exists():
                    new_id += 1
                else:
                    break
            product.Product_ID.Stock -= 1
            product.Product_ID.save()
            today = date.today()
            query = Order()
            query.Order_ID = new_id
            query.Order_date = today
            query.Customer_ID = request.user
            query.Product_ID = product.Product_ID
            if product.Buy_Or_Rent:
                query.Amount = product.Product_ID.Sell_Price
            else:
                query.Amount = product.Product_ID.Rent_Price * 7
            # query.Delivery_ID = new_id
            query.Shop_ID = product.Product_ID.Shop_ID
            query.First_Name = request.POST.get("fname")
            query.Last_Name = request.POST.get("lname")
            query.Email = request.POST.get("Email")
            query.Phone = request.POST.get("Phone")
            query.Address = request.POST.get("Address")
            query.State = request.POST.get("State")
            query.City = request.POST.get("City")
            query.ZIP = request.POST.get("Zip")
            product.delete()
            query.save()
        return redirect('cardpage')
    return render(request, 'Store/paymentpage.html', context)


@login_required
def successfullyPaid(request):
    return render(request, 'Store/SuccessfullyPaid.html')


@login_required
def card_page(request):
    if request.method == 'POST':
        return redirect('successfullyPaid')
    return render(request, 'Store/CardPage.html')


@login_required
def delete_cart(request, cart_id):
    cart_to_delete = Cart.objects.all().get(Cart_ID=cart_id)
    cart_to_delete.delete()
    return redirect('paymentpage')


@login_required
def cart_buy(request, id):
    product = Products.objects.all().get(Product_ID=id)

    if in_cart(request.user, product):
        return redirect('product_info', id)

    cart = Cart()
    new_id = 1
    while True:
        if Cart.objects.filter(Cart_ID=new_id).exists():
            new_id += 1
        else:
            break
    cart.Cart_ID = new_id
    cart.Customer_ID = request.user
    cart.Product_ID = product
    cart.Buy_Or_Rent = True
    cart.save()
    return redirect('product_info', id)


@login_required
def cart_rent(request, id):
    product = Products.objects.all().get(Product_ID=id)

    if in_cart(request.user, product):
        return redirect('product_info', id)

    cart = Cart()
    new_id = 1
    while True:
        if Cart.objects.filter(Cart_ID=new_id).exists():
            new_id += 1
        else:
            break
    cart.Cart_ID = new_id
    cart.Customer_ID = request.user
    cart.Product_ID = product
    cart.Buy_Or_Rent = False
    cart.save()
    return redirect('product_info', id)


def in_cart(user, product):
    carts = Cart.objects.all()
    for cart in carts:
        if cart.Product_ID == product and cart.Customer_ID == user:
            return True
    return False


def productpage(request):
    product = Products.objects.all()
    media = Media.objects.all()
    productdescription = Product_Description.objects.select_related("Product_ID")
    product_media = Media.objects.select_related("Product_ID")
    shop = Shop.objects.all()
    review = Review.objects.all()

    context = {
        "products": product,
        "medias": media,
        "product_media": product_media,
        "productdescriptions": productdescription,
        "shops": shop,
        "reviews": review,
    }
    return render(request, 'Store/productpage.html', context)


def update_variable(value):
    """Allows to update existing variable in template"""
    return value


def product_info(request, product_id):
    product = Products.objects.get(Product_ID=product_id)
    photos = Media.objects.all().filter(Product_ID=product)
    info = Product_Description.objects.get(Product_ID=product)
    incart = in_cart(request.user, product)
    shop_products = Products.objects.all().filter(Shop_ID=product.Shop_ID)
    media = Media.objects.all()
    reviews = Review.objects.all().filter(Reviewee=product.Shop_ID.User_ID)[:3]
    context = {
        "product": product,
        "photos": photos,
        "info": info,
        "incart": incart,
        "shop_products": shop_products,
        "media": media,
        "reviews": reviews,
        "size": reviews.count(),
    }
    return render(request, 'Store/ProductInfoPage.html', context)


# function to view all reviews


def get_reviews(request):
    reviews = Review.objects.all()

    return render(request, 'Store/homepage.html', {'reviews': reviews})


def blog_page(request):
    blogs = Blog.objects.all().values()
    user_info = request.user
    if request.method == 'POST':
        email_message = request.POST.get("msg")
        email_subject = "[Suggestion]"
        send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
        return render(request, 'Store/blog.html',
                      {
                          'blogs': blogs,
                          'user': user_info
                      })
    return render(request, 'Store/blog.html',
                  {
                      'blogs': blogs,
                      'user': user_info
                  })


# ---------- #
# Function to post a new blog as admin
def postBlog(request):
    # Post blog form
    if request.method == 'POST':
        # New Blog object
        post = Blog()

        # generate new non-existing Rating_ID (0 is default - never start from 0)
        new_id = 1
        while True:
            if Blog.objects.filter(Blog_ID=new_id).exists():
                new_id += 1
            else:
                break

        # Set values to new review obj
        post.Blog_ID = new_id
        post.Title = request.POST.get("blog_title")
        post.Preview = request.POST.get("blog_preview")
        post.Blog_URL = request.POST.get("blog_link")
        post.Image_URL = request.POST.get("blog_image")

        # Commit the review obj to DB
        post.save()

        # Return user to order history page
        return redirect(request.META.get('HTTP_REFERER', '/blogs'))
    return HttpResponse(status=204)


# ---------- #
# Function to remove a blog as admin
def postBlogRemove(request):
    if request.method == 'POST':
        Blog.objects.filter(Blog_ID=request.POST.get("blog_id")).delete()

        # Return user to order history page
        return redirect(request.META.get('HTTP_REFERER', '/blogs'))

    return HttpResponse(status=204)


# ---------- #
# Function to add a new self-written blog
def postSelfBlogAdd(request):
    # Post blog form
    if request.method == 'POST':

        # New Blog object
        post = Blog()

        # generate new non-existing Rating_ID (0 is default - never start from 0)
        new_id = 1
        while True:
            if Blog.objects.filter(Blog_ID=new_id).exists():
                new_id += 1
            else:
                break

        # Set values to new review obj
        post.Blog_ID = new_id
        post.Title = request.POST.get("self_blog_title")
        post.Preview = request.POST.get("self_blog_text")
        post.Image_URL = request.POST.get("self_blog_image")
        post.Self_Written = True

        # Commit the review obj to DB
        post.save()

        # Return user to order history page
        return redirect(request.META.get('HTTP_REFERER', '/blogs'))
    return HttpResponse(status=204)


def contact_view(request):
    if request.method == 'POST':
        query = Contact()
        query.First_Name = request.POST.get("First_Name")
        query.Last_Name = request.POST.get("Last_Name")
        query.Email = request.POST.get("Email")
        query.Subject = request.POST.get("Subject")
        query.Message = request.POST.get("Message")
        query.save()
        email_subject = f'[New contact message] {query.Subject}'
        email_name = f'Name: {query.First_Name} {query.Last_Name}'
        email_customer = f'Email: {query.Email}'
        courtesy_msg = 'You received a new message from your online store\'s contact form.'
        email_message = f'{courtesy_msg}\n{email_name}\n{email_customer}\nMessage: {query.Message}'
        send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
        return render(request, 'Store/contact_success.html')
    return render(request, 'Store/ContactUs.html')
