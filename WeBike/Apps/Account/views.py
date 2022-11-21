from __future__ import print_function

from http.client import HTTPResponse
from math import prod
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import NewUser
from Store.models import Shop, Products, Media, Product_Description
from .forms import LogInForm, RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from Store.models import Products, Review
from .forms import RegisterForm
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
import Store

import traceback
import sys


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy("login")
    template_name = 'Account/register.html'


class LoginView(generic.FormView):
    template_name = 'Account/login.html'
    form_class = AuthenticationForm
    success_url = '../../'
    # home page


class ForgotPasswordView(generic.TemplateView):
    model = NewUser
    template_name = 'Account/forgotpassword.html'


class SuccessUserCreationView(generic.TemplateView):
    model = NewUser
    template_name = 'Account/successcreation.html'


# def shoppage(request):
#     shop_products = Products.objects.all()
#     return render(request,
#                   'Account/shoppage.html', {
#                       'shop_products': shop_products
#                   })


@login_required
def userpage(request):
    # Get first 3 reviews for logged in user
    review = Review.objects.all().filter(Reviewee=request.user)[:3]
    # get user shop flag
    shop = Shop.objects.filter(User_ID=request.user).count()
    # Check size
    if review.count() == 0:
        context = {
            "shop": shop,
        }
        return render(request, 'Account/userpage.html', context)
    else:
        context = {
            "reviews": review,
            "size": review.count(),
            "shop": shop,
        }
        return render(request, 'Account/userpage.html', context)


@login_required
def shoppage(request):
    shop = Shop.objects.get(User_ID=request.user)
    products = Products.objects.filter(Shop_ID=shop)
    shops = Shop.objects.all()
    abns = []
    for each in shops:
        abns.append(each.ABN)
    review = Review.objects.all().filter(Reviewee=request.user)[:3]
    medias = Media.objects.all()
    descriptions = Product_Description.objects.all()   
    if review.count() == 0:
        context = {
            "products": products,
            "shop": shop,
            "medias": medias,
            "descriptions": descriptions,
            "abns": abns,
        }
    else:
        context = {
            "reviews": review,
            "size": review.count(),
            "products": products,
            "shop": shop,
            "medias": medias,
            "descriptions": descriptions,
            "abns": abns,
        }
    # context = {
    #     "products": products,
    #     "shop": shop,
    #     "medias": medias,
    #     "descriptions": descriptions,
    # }
    return render(request, 'Account/shoppage.html', context)


@login_required
def userpage(request):
    # Get first 3 reviews for logged in user
    review = Review.objects.all().filter(Reviewee=request.user)[:3]
    # get user shop flag
    shop = Shop.objects.filter(User_ID=request.user).count()
    # Check size
    if review.count() == 0:
        context = {
            "shop": shop,
        }
        return render(request, 'Account/userpage.html', context)
    else:
        context = {
            "reviews": review,
            "size": review.count(),
            "shop": shop,
        }
        return render(request, 'Account/userpage.html', context)


@login_required
def shoppage(request):
    shop = Shop.objects.get(User_ID=request.user)
    products = Products.objects.filter(Shop_ID=shop)
    print(shop)
    medias = Media.objects.all()
    descriptions = Product_Description.objects.all()
    context = {
        "products": products,
        "shop": shop,
        "medias": medias,
        "descriptions": descriptions,
    }
    return render(request, 'Account/shoppage.html', context)


@login_required
def submit_info(request):
    if request.method == "POST":
        data = request.POST  # data
        # avatar
        file = request.FILES['avatar'] if 'avatar' in request.FILES else None
        user = request.user  # current user
        # not null
        if data['fname'] != "":
            user.first_name = data['fname']
        if data['lname'] != "":
            user.last_name = data['lname']
        if data['phone'] != "":
            user.phone_number = data['phone']
        if file:
            # file system
            fss = FileSystemStorage()
            # remove existed photo
            if user.image_location:
                fss.delete(user.email + "_avatar.png")
            # save and get url
            avatar = fss.save(user.email + "_avatar.png", file)
            user.image_location = fss.url(avatar)
        # update current user
        user.save()
        # redirect
        return redirect('userpage')

    return render(request, 'Account/userpage.html')


@login_required
def shop_submit_info(request):
    if request.method == "POST":
        data = request.POST  # data
        file_logo = request.FILES['slogo'] if 'slogo' in request.FILES else None
        file_banner = request.FILES['sbanner'] if 'sbanner' in request.FILES else None
        shop = Shop.objects.get(User_ID=request.user)

        if data['sname'] != "":
            shop.Business_Name = data['sname']
        if data['semail'] != "":
            shop.Business_Email = data['semail']
        if data['sphone'] != "":
            shop.Business_Number = data['sphone']
        if data['slocation'] != "":
            shop.Location = data['slocation']
        if data['swebsite'] != "":
            shop.Business_URL = data['swebsite']
        if data['sABN'] != "":
            shop.ABN = data['sABN']
        if data['sintro'] != "":
            shop.Description = data['sintro']

        if file_logo:
            # file system
            fss1 = FileSystemStorage()
            # remove existed photo
            if shop.Logo_URL:
                print(shop.Logo_URL[7:])
                fss1.delete(shop.Logo_URL[7:])
            # save and get url
            shoplogo = fss1.save(shop.Business_Name +
                                 str(shop.ABN) + "_shop_logo", file_logo)
            shop.Logo_URL = fss1.url(shoplogo)

        if file_banner:
            # file system
            fss2 = FileSystemStorage()
            # remove existed photo
            if shop.Banner_URL:
                print(shop.Banner_URL[7:])
                fss2.delete(shop.Banner_URL[7:])
            # save and get url
            shopbanner = fss2.save(
                shop.Business_Name + str(shop.ABN) + "_shop_banner", file_banner)
            shop.Banner_URL = fss2.url(shopbanner)
        # update current shop
        shop.save()
        return redirect('shoppage')
    return render(request, 'Account/shoppage.html')


@login_required
def product_submit_info(request, id):
    product = Products.objects.get(Product_ID=id)
    photos = Media.objects.all().filter(Product_ID=product)
    # photo1 = photos[0]
    description = Product_Description.objects.get(Product_ID=product)
    img1 = request.FILES['img1'] if 'img1' in request.FILES else None
    img2 = request.FILES['img2'] if 'img2' in request.FILES else None
    img3 = request.FILES['img3'] if 'img3' in request.FILES else None
    img4 = request.FILES['img4'] if 'img4' in request.FILES else None
    img5 = request.FILES['img5'] if 'img5' in request.FILES else None
    if request.method == "POST":
        data = request.POST  # data
        if data['pname'] != "":
            product.Product_name = data['pname']
        if data['productsellprice'] != "":
            product.Sell_Price = data['productsellprice']
        if data['productrentprice'] != "":
            product.Rent_Price = data['productrentprice']
        if data['psponsorstatus'] != "":
            product.Sponsor_Status = data['psponsorstatus']
        if data['productstock'] != "":
            product.Stock = data['productstock']
        if data['description'] != "":
            description.Description = data['description']
        if data['ptype'] != "":
            description.Type = data['ptype']
        if data['pagerange'] != "":
            description.Age_Range = data['pagerange']
        if data['pbrand'] != "":
            description.Brand = data['pbrand']
        if data['pspeed'] != "":
            description.Speeds = data['pspeed']
        if data['pcolor'] != "":
            description.Colour = data['pcolor']
        if img1:
            # file system
            fss1 = FileSystemStorage()
            if len(photos) >= 1:
                photo1 = photos[0]
                if photo1.Storage_location:
                    fss1.delete(photo1.Storage_location[7:])
                # save and get url
                img = fss1.save(str(product.Product_ID) + "_img1", img1)
                photo1.Storage_location = fss1.url(img)
                product.save()
                description.save()
                photo1.save()
            else:
                fss1 = FileSystemStorage()
                media = Media()
                new_id = 1
                while True:
                    if Media.objects.filter(Media_ID=new_id).exists():
                        new_id += 1
                    else:
                        break

                media.Media_ID = new_id
                media.Product_ID = product
                # save and get url
                image1 = fss1.save(str(product.Product_ID) + "_img1", img1)
                media.Storage_location = fss1.url(image1)
                product.save()
                description.save()
                media.save()
        if img2:
            # file system
            fss1 = FileSystemStorage()
            if len(photos) >= 2:
                photo1 = photos[1]
                if photo1.Storage_location:
                    fss1.delete(photo1.Storage_location[7:])
                # save and get url
                img = fss1.save(str(product.Product_ID) + "_img2", img2)
                photo1.Storage_location = fss1.url(img)
                product.save()
                description.save()
                photo1.save()
            else:
                fss1 = FileSystemStorage()
                media = Media()
                new_id = 1
                while True:
                    if Media.objects.filter(Media_ID=new_id).exists():
                        new_id += 1
                    else:
                        break

                media.Media_ID = new_id
                media.Product_ID = product
                # save and get url
                image1 = fss1.save(str(product.Product_ID) + "_img2", img2)
                media.Storage_location = fss1.url(image1)
                product.save()
                description.save()
                media.save()
        if img3:
            # file system
            fss1 = FileSystemStorage()
            if len(photos) >= 3:
                photo1 = photos[2]
                if photo1.Storage_location:
                    fss1.delete(photo1.Storage_location[7:])
                # save and get url
                img = fss1.save(str(product.Product_ID) + "_img3", img3)
                photo1.Storage_location = fss1.url(img)
                product.save()
                description.save()
                photo1.save()
            else:
                fss1 = FileSystemStorage()
                media = Media()
                new_id = 1
                while True:
                    if Media.objects.filter(Media_ID=new_id).exists():
                        new_id += 1
                    else:
                        break

                media.Media_ID = new_id
                media.Product_ID = product
                # save and get url
                image1 = fss1.save(str(product.Product_ID) + "_img3", img3)
                media.Storage_location = fss1.url(image1)
                product.save()
                description.save()
                media.save()
        if img4:
            # file system
            fss1 = FileSystemStorage()
            if len(photos) >= 4:
                photo1 = photos[3]
                if photo1.Storage_location:
                    fss1.delete(photo1.Storage_location[7:])
                # save and get url
                img = fss1.save(str(product.Product_ID) + "_img4", img4)
                photo1.Storage_location = fss1.url(img)
                product.save()
                description.save()
                photo1.save()
            else:
                fss1 = FileSystemStorage()
                media = Media()
                new_id = 1
                while True:
                    if Media.objects.filter(Media_ID=new_id).exists():
                        new_id += 1
                    else:
                        break

                media.Media_ID = new_id
                media.Product_ID = product
                # save and get url
                image1 = fss1.save(str(product.Product_ID) + "_img4", img4)
                media.Storage_location = fss1.url(image1)
                product.save()
                description.save()
                media.save()
        if img5:
            # file system
            fss1 = FileSystemStorage()
            if len(photos) >= 5:
                photo1 = photos[4]
                if photo1.Storage_location:
                    fss1.delete(photo1.Storage_location[7:])
                # save and get url
                img = fss1.save(str(product.Product_ID) + "_img5", img5)
                photo1.Storage_location = fss1.url(img)
                product.save()
                description.save()
                photo1.save()
            else:
                fss1 = FileSystemStorage()
                media = Media()
                new_id = 1
                while True:
                    if Media.objects.filter(Media_ID=new_id).exists():
                        new_id += 1
                    else:
                        break

                media.Media_ID = new_id
                media.Product_ID = product
                # save and get url
                image1 = fss1.save(str(product.Product_ID) + "_img5", img5)
                media.Storage_location = fss1.url(image1)
                product.save()
                description.save()
                media.save()

        product.save()
        description.save()
        return redirect('shoppage')
    return render(request, 'Account/shoppage.html')


@login_required
def add_product_info(request):
    shop = Shop.objects.get(User_ID=request.user)
    img1 = request.FILES['img1'] if 'img1' in request.FILES else None
    img2 = request.FILES['img2'] if 'img2' in request.FILES else None
    img3 = request.FILES['img3'] if 'img3' in request.FILES else None
    img4 = request.FILES['img4'] if 'img4' in request.FILES else None
    img5 = request.FILES['img5'] if 'img5' in request.FILES else None
    product = Products()
    new_id = 1
    while True:
        if Products.objects.filter(Product_ID=new_id).exists():
            new_id += 1
        else:
            break

    product.Product_ID = new_id
    product.Shop_ID = shop
    description = Product_Description()
    description.Product_ID = product
    if request.method == "POST":
        data = request.POST  # data
        if data['pname'] != "":
            product.Product_name = data['pname']
        if data['productsellprice'] != "":
            product.Sell_Price = data['productsellprice']
        if data['productrentprice'] != "":
            product.Rent_Price = data['productrentprice']
        if data['psponsorstatus'] != "":
            product.Sponsor_Status = data['psponsorstatus']
        if data['productstock'] != "":
            product.Stock = data['productstock']
        if data['description'] != "":
            description.Description = data['description']
        if data['ptype'] != "":
            description.Type = data['ptype']
        if data['pagerange'] != "":
            description.Age_Range = data['pagerange']
        if data['pbrand'] != "":
            description.Brand = data['pbrand']
        if data['pspeed'] != "":
            description.Speeds = data['pspeed']
        if data['pcolor'] != "":
            description.Colour = data['pcolor']

        if img1:
            # file system
            fss1 = FileSystemStorage()
            media = Media()
            new_id = 1
            while True:
                if Media.objects.filter(Media_ID=new_id).exists():
                    new_id += 1
                else:
                    break

            media.Media_ID = new_id
            media.Product_ID = product
            # save and get url
            image1 = fss1.save(str(product.Product_ID) + "_img1", img1)
            media.Storage_location = fss1.url(image1)
            product.save()
            description.save()
            media.save()

        if img2:
            # file system
            fss1 = FileSystemStorage()
            media = Media()
            new_id = 1
            while True:
                if Media.objects.filter(Media_ID=new_id).exists():
                    new_id += 1
                else:
                    break

            media.Media_ID = new_id
            media.Product_ID = product
            # save and get url
            image2 = fss1.save(str(product.Product_ID) + "_img2", img2)
            media.Storage_location = fss1.url(image2)
            product.save()
            description.save()
            media.save()

        if img3:
            # file system
            fss1 = FileSystemStorage()
            media = Media()
            new_id = 1
            while True:
                if Media.objects.filter(Media_ID=new_id).exists():
                    new_id += 1
                else:
                    break

            media.Media_ID = new_id
            media.Product_ID = product
            # save and get url
            image = fss1.save(str(product.Product_ID) + "_img3", img3)
            media.Storage_location = fss1.url(image)
            product.save()
            description.save()
            media.save()

        if img4:
            # file system
            fss1 = FileSystemStorage()
            media = Media()
            new_id = 1
            while True:
                if Media.objects.filter(Media_ID=new_id).exists():
                    new_id += 1
                else:
                    break

            media.Media_ID = new_id
            media.Product_ID = product
            # save and get url
            image2 = fss1.save(str(product.Product_ID) + "_img4", img4)
            media.Storage_location = fss1.url(image2)
            product.save()
            description.save()
            media.save()

        if img5:
            # file system
            fss1 = FileSystemStorage()
            media = Media()
            new_id = 1
            while True:
                if Media.objects.filter(Media_ID=new_id).exists():
                    new_id += 1
                else:
                    break

            media.Media_ID = new_id
            media.Product_ID = product
            # save and get url
            image2 = fss1.save(str(product.Product_ID) + "_img5", img5)
            media.Storage_location = fss1.url(image2)
            product.save()
            description.save()
            media.save()

        product.save()
        description.save()
        # media.save()
        return redirect('shoppage')

    return render(request, 'Account/shoppage.html')


@login_required
def deactivate(request, id):
    product = Products.objects.get(Product_ID=id)
    if request.method == "POST":
        data = request.POST  # data
        product.Is_Available = False
        product.save()
        return redirect('shoppage')

    return render(request, 'Account/shoppage.html')


@login_required
def activate(request, id):
    product = Products.objects.get(Product_ID=id)
    if request.method == "POST":
        data = request.POST  # data
        product.Is_Available = True
        product.save()
        return redirect('shoppage')

    return render(request, 'Account/shoppage.html')


def orderHistory(request):
    order_all = Store.models.Order.objects.all()
    media_all = Store.models.Media.objects.all()
    reviews_all = Store.models.Review.objects.all()

    if request.user.is_authenticated:
        current_user = request.user
        order_filtered = order_all.filter(Customer_ID=current_user.id)
        reviews_filtered = reviews_all.filter(Reviewer=current_user.id)
        shop = Shop.objects.filter(User_ID=request.user).count()

        context = {
            'order': order_filtered,
            'media': media_all,
            'reviews': reviews_filtered,
            'shop': shop,
        }

        return render(request, 'Account/orderHistory.html', context)

    else:
        # Error case - return login page
        return render(request, 'Account/login.html')


def postReview(request):
    # Post review form
    if request.method == 'POST':

        # New review object
        post = Review()

        # generate new non-existing Rating_ID (0 is default - never start from 0)
        new_id = 1
        while True:
            if Review.objects.filter(Rating_ID=new_id).exists():
                new_id += 1
            else:
                break

        # Set values to new review obj
        post.Rating_ID = new_id
        post.Reviewer = request.user
        post.Reviewee = NewUser.objects.get(
            email=request.POST.get('seller_email'))
        post.Comment = request.POST.get('comment')
        post.Rating_value = request.POST.get('rating')

        # Check to see if the user has already reviewd the seller - if yes, update
        for item in Review.objects.all():
            if item.Reviewer == post.Reviewer and item.Reviewee == post.Reviewee:
                # overwrite
                item.Comment = post.Comment
                item.Rating_value = post.Rating_value
                item.save()
                return redirect(request.META['HTTP_REFERER'])

        # Commit the review obj to DB
        post.save()

        # Return user to order history page
        return redirect(request.META['HTTP_REFERER'])
    return HttpResponse(status=204)


@login_required
def shopsetup(request):
    shops = Shop.objects.all()
    abns = []
    for shop in shops:
        abns.append(shop.ABN)
    context = {"abns": abns}
    return render(request, 'Account/setupshop.html', context)


@login_required
def setupshop(request):
    if request.method == 'POST':
        if (request.POST.get('abn') and request.POST.get('detail-confirm') and request.POST.get(
                'location') and request.POST.get('email') and request.POST.get('phone')):
            # Instantiate FSS object
            fss = FileSystemStorage()

            # Create new shop instance
            post = Shop()

            # Check if logo uploaded
            if 'logo' in request.FILES:
                logo_upload = request.FILES['logo']
                logo_file = fss.save(logo_upload.name, logo_upload)
                logo_url = fss.url(logo_file)
                post.Logo_URL = logo_url

            # Check if header uploaded
            if 'header_img' in request.FILES:
                header_upload = request.FILES['header_img']
                header_file = fss.save(header_upload.name, header_upload)
                header_url = fss.url(header_file)
                post.Banner_URL = header_url

            # generate new non-existing ID (0 is default - never start from 0)
            new_id = 1
            while True:
                if Shop.objects.filter(Shop_ID=new_id).exists():
                    new_id += 1
                else:
                    break

            post.Shop_ID = new_id

            # Get logged in users id
            post.User_ID = request.user

            # Post shop details
            post.Business_Number = request.POST.get('phone')
            post.Business_Email = request.POST.get('email')
            post.Location = request.POST.get('location')
            post.ABN = request.POST.get('abn')
            post.Business_URL = request.POST.get('url')
            post.Description = request.POST.get('description')
            post.Business_Name = request.POST.get('shop_name')
            post.save()
            return redirect('shoppage')
    else:
        return redirect('shoppage')

        # Failed validation checks
    return HttpResponse(status=204)
