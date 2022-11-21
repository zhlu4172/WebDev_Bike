import unittest

from django.test import TestCase, Client
from .models import Products, Product_Description, Shop, Cart, Contact, Blog
from Account.models import NewUser

from .views import in_cart


# Create your tests here.
class StoreTests(TestCase):
    def setUp(self):
        NewUser.objects.create_user(email="StoreTest@test.com", password="123456")
        new_user = NewUser.objects.get(email="StoreTest@test.com")
        Shop.objects.create(Shop_ID=1, User_ID=new_user)
        shop = Shop.objects.get(Shop_ID=1)
        Products.objects.create(Product_ID=1, Shop_ID=shop)
        product = Products.objects.get(Product_ID=1)
        Product_Description.objects.create(Product_ID=product)

    def test_productInfo_request(self):
        client = Client()
        response = client.get("/productinfo/1/")
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed('Store/ProductInfoPage.html')

    @unittest.expectedFailure
    def test_productInfo_InvalidId(self):
        client = Client()
        client.get("/productinfo/-1/")

    def test_productInfo_NoId(self):
        client = Client()
        response = client.get("/productinfo/")
        self.assertEqual(404, response.status_code)

    def test_cart_buy(self):
        new_user = NewUser.objects.get(email="StoreTest@test.com")
        product = Products.objects.get(Product_ID=1)
        self.assertFalse(in_cart(new_user, product))
        client = Client()
        client.login(email="StoreTest@test.com", password="123456")
        response = client.get("/buy/1")
        self.assertEqual(302, response.status_code)
        self.assertTrue(in_cart(new_user, product))

    def test_cart_remove(self):
        client = Client()
        client.login(email="StoreTest@test.com", password="123456")
        client.get("/buy/1")
        new_user = NewUser.objects.get(email="StoreTest@test.com")
        product = Products.objects.get(Product_ID=1)
        self.assertTrue(in_cart(new_user, product))
        cart = Cart.objects.get(Customer_ID=new_user)
        response = client.get("/payment/remove/" + str(cart.Cart_ID))
        self.assertEqual(302, response.status_code)
        self.assertFalse(in_cart(new_user, product))

    def test_cart_rent(self):
        client = Client()
        client.login(email="StoreTest@test.com", password="123456")
        client.get("/buy/1")
        new_user = NewUser.objects.get(email="StoreTest@test.com")
        product = Products.objects.get(Product_ID=1)
        cart = Cart.objects.get(Customer_ID=new_user)
        client.get("/payment/remove/" + str(cart.Cart_ID))
        self.assertFalse(in_cart(new_user, product))
        response = client.get("/rent/1")
        self.assertEqual(302, response.status_code)
        self.assertTrue(in_cart(new_user, product))

    def test_payment_display(self):
        client = Client()
        response = client.get("/payment/")
        self.assertEqual(302, response.status_code)
        client.login(email="StoreTest@test.com", password="123456")
        response = client.get("/payment/")
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed('Store/paymentpage.html')

    def test_finish_payment(self):
        client = Client()
        client.login(email="StoreTest@test.com", password="123456")
        client.get("/buy/1")
        product_stock = Products.objects.get(Product_ID=1).Stock
        cart_size = len(Cart.objects.all())
        response = client.post("/payment/", {"fname": "", "lname": "", "Email": "paymentTest@test.com", "Phone": 123,
                                             "Address": "", "State": "test", "City": "test", "Zip": 2008})
        self.assertEqual(302, response.status_code)
        new_product_stock = Products.objects.get(Product_ID=1).Stock
        new_cart_size = len(Cart.objects.all())
        self.assertEqual(product_stock - 1, new_product_stock)
        self.assertEqual(cart_size - 1, new_cart_size)

    def test_card_successfully_display(self):
        client = Client()
        client.login(email="StoreTest@test.com", password="123456")
        client.get("/buy/1")
        response = client.post("/payment/", {"fname": "", "lname": "", "Email": "paymentTest@test.com", "Phone": 123,
                                             "Address": "", "State": "test", "City": "test", "Zip": 2008})
        self.assertEqual(302, response.status_code)
        self.assertTemplateUsed('Store/CardPage.html')
        response = client.post("/cardpage/", {"Number": 1234123412341234, "Name": "", "Expiry": "", "CVV": 123})
        self.assertEqual(302, response.status_code)
        self.assertTemplateUsed('Store/SuccessfullyPaid.html')

    def test_card_without_login(self):
        client = Client()
        client.get("/cardpage/")
        self.assertTemplateUsed('registration/login.html')

    def test_successfully_without_login(self):
        client = Client()
        client.get("/successfullyPaid/")
        self.assertTemplateUsed('registration/login.html')


    #Home page success test - guest
    def test_homepage(self):
        client = Client('')
        #lands on homepage
        self.assertTemplateUsed('Store/homepage.html')

    # #Home page request success test - logged in
    def test_homepage_loggedin(self):
        client = Client()
        client.login(email="StoreTest@test.com", password="123456")
        #lands on homepage
        self.assertTemplateUsed('Store/homepage.html')

    def test_contact_us(self):
        client = Client()
        response = client.post("/contactus/", {"First_Name": "Tester", "Last_Name": "Laster", "Email": "contactTest@test.com",
                                             "Subject": "Feedback", "Message": "Your website is quite good!"})
        self.assertEqual(200, response.status_code)
        subject = Contact.objects.get(Email="contactTest@test.com").Subject
        first_name = Contact.objects.get(Email="contactTest@test.com").First_Name
        last_name = Contact.objects.get(Email="contactTest@test.com").Last_Name
        message = Contact.objects.get(Email="contactTest@test.com").Message
        email = Contact.objects.get(Email="contactTest@test.com").Email
        self.assertEqual(subject, "Feedback")
        self.assertEqual(first_name, "Tester")
        self.assertEqual(last_name, "Laster")
        self.assertEqual(message, "Your website is quite good!")
        self.assertEqual(email, "contactTest@test.com")

    def test_blogpage(self):
        client = Client()
        response = client.get("/blog/")
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed('Store/blog.html')

    def test_add_blog(self):
        client = Client()
        client.login(email='test@test.com', password='test')
       
        client.get('/blog')
        client.post('/postBlog/', 
        {"blog_title": "Title", "blog_preview": "preview",
        "blog_link": "https/link.com", "blog_image": "img.png"})

        blog = Blog.objects.get(Title="Title")
        self.assertEqual("Title", blog.Title)
        self.assertEqual("preview", blog.Preview)
        self.assertEqual("https/link.com", blog.Blog_URL)
        self.assertEqual("img.png", blog.Image_URL)
        self.assertEqual(1, blog.Blog_ID)

    @unittest.expectedFailure
    def test_remove_blog(self):
        client = Client()
        client.login(email='test@test.com', password='test')

        client.get('/blog')
        client.post('/postBlog/', 
        {"blog_title": "Title", "blog_preview": "preview",
        "blog_link": "https/link.com", "blog_image": "img.png"})

        client.post('/postBlogRemove/', {"blog_id": "1"})
        Blog.objects.get(Blog_ID="1")

    def test_selfwritten_add(self):
        client = Client()
        client.login(email='test@test.com', password='test')
        client.get('/blog')

        client.post('/postSelfBlogAdd/', 
        {"self_blog_title": "My Blog",
        "self_blog_image": "img",
        "self_blog_text": "This is my own blog"
        })

        Blog.objects.get(Title="My Blog")



