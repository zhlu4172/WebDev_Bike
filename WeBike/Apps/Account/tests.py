from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from .models import NewUser
from Store.models import Products, Product_Description, Shop, Cart, Order


class UserAccountTests(TestCase):

    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'testuser@super.com', 'password')
        self.assertEqual(super_user.email, 'testuser@super.com')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_admin)
        self.assertTrue(super_user.is_active)

    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user(
            'testuser@user.com', 'password')
        self.assertEqual(user.email, 'testuser@user.com')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_admin)
        self.assertTrue(user.is_active)


class UserTests(TestCase):
    def setUp(self):
        NewUser.objects.create_superuser(email='test@test.com', password='test')
        new_user = NewUser.objects.get(email="test@test.com")
        Shop.objects.create(Shop_ID=1, User_ID=new_user)
        shop = Shop.objects.get(Shop_ID=1)
        Products.objects.create(Product_ID=1, Shop_ID=shop)
        product = Products.objects.get(Product_ID=1)
        Product_Description.objects.create(Product_ID=product)

    def test_loginUser(self):
        client = Client()
        client.login(email='test@test.com', password='test')
        response = client.get('/account/profile/')
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'Account/userpage.html')

    def test_unLoginUser(self):
        client = Client()
        response = client.get('/account/profile/')
        self.assertEqual(302, response.status_code)
        self.assertTemplateNotUsed(response, 'Account/userpage.html')

    def test_submitInfo(self):
        client = Client()
        client.login(email='test@test.com', password='test')
        response = client.post('/account/profile/edit', {"fname": "Mr Test", "lname": "", "phone": "123"})
        new_user = NewUser.objects.all().get(email='test@test.com')
        self.assertEqual("Mr Test", new_user.first_name)
        self.assertEqual("", new_user.last_name)
        self.assertEqual("123", new_user.phone_number)
        self.assertEqual(302, response.status_code)

    def test_submitTwice(self):
        client = Client()
        client.login(email='test@test.com', password='test')
        response = client.post('/account/profile/edit', {"fname": "Mr Test", "lname": "", "phone": "123"})
        response = client.post('/account/profile/edit', {"fname": "", "lname": "Mr Test", "phone": ""})
        new_user = NewUser.objects.all().get(email='test@test.com')
        self.assertEqual("Mr Test", new_user.first_name)
        self.assertEqual("Mr Test", new_user.last_name)
        self.assertEqual("123", new_user.phone_number)
        self.assertEqual(302, response.status_code)

    def test_shop(self):
        client = Client()
        client.login(email='test@test.com', password='test')
        response = client.post('/account/shop/edit',
                               {"sname": "Test Store", "semail": "teststore@test.com", "sphone": "0400000000",
                                "slocation": "sydney", "swebsite": "https://www.sydney.edu.au/", "sABN": "15211513464",
                                "sintro": "testintro"})
        user = NewUser.objects.all().get(email='test@test.com')
        shop = Shop.objects.all().get(User_ID=user)
        self.assertEqual("sydney", shop.Location)
        self.assertEqual(15211513464, shop.ABN)
        self.assertEqual("teststore@test.com", shop.Business_Email)
        self.assertEqual("0400000000", shop.Business_Number)
        self.assertEqual("https://www.sydney.edu.au/", shop.Business_URL)
        self.assertEqual("testintro", shop.Description)
        self.assertEqual("Test Store", shop.Business_Name)
        self.assertEqual(302, response.status_code)

    def test_shopWithEmptyInput(self):
        client = Client()
        client.login(email='test@test.com', password='test')
        response = client.post('/account/shop/edit',
                               {"sname": "Test Store", "semail": "teststore@test.com", "sphone": "",
                                "slocation": "", "swebsite": "https://www.sydney.edu.au/", "sABN": "15211513464",
                                "sintro": "testintro"})
        user = NewUser.objects.all().get(email='test@test.com')
        shop = Shop.objects.all().get(User_ID=user)
        self.assertEqual("", shop.Location)
        self.assertEqual(15211513464, shop.ABN)
        self.assertEqual("teststore@test.com", shop.Business_Email)
        self.assertEqual("", shop.Business_Number)
        self.assertEqual("https://www.sydney.edu.au/", shop.Business_URL)
        self.assertEqual("testintro", shop.Description)
        self.assertEqual("Test Store", shop.Business_Name)
        self.assertEqual(302, response.status_code)

    def test_addProduct(self):
        client = Client()
        client.login(email='test@test.com', password='test')
        response = client.post('/account/shop/addproduct',
                               {"pname": "product test", "productsellprice": 1200, "productrentprice": 80,
                                "psponsorstatus": False, "productstock": 10, "description": "test description",
                                "ptype": "test type", "pagerange": "testrange", "pbrand": "test brand", "pspeed": 40,
                                "pcolor": "red"})
        product = Products.objects.get(Product_name="product test")
        product_description = Product_Description.objects.get(Product_ID=product)
        self.assertEqual("product test", product.Product_name)
        self.assertEqual(1200, product.Sell_Price)
        self.assertEqual(80, product.Rent_Price)
        self.assertEqual(10, product.Stock)
        self.assertEqual(False, product.Sponsor_Status)
        self.assertEqual("test type", product_description.Type)
        self.assertEqual("testrange", product_description.Age_Range)
        self.assertEqual("test brand", product_description.Brand)
        self.assertEqual("red", product_description.Colour)
        self.assertEqual(40, product_description.Speeds)
        self.assertEqual(302, response.status_code)

    def test_editProduct(self):
        client = Client()
        client.login(email='test@test.com', password='test')
        response = client.post('/account/shop/editproduct/1',
                               {"pname": "product test", "productsellprice": 1200, "productrentprice": 80,
                                "psponsorstatus": False, "productstock": 10, "description": "test description",
                                "ptype": "test type", "pagerange": "testrange", "pbrand": "test brand", "pspeed": 40,
                                "pcolor": "red"})
        product = Products.objects.get(Product_ID=1)
        product_description = Product_Description.objects.get(Product_ID=product)
        self.assertEqual("product test", product.Product_name)
        self.assertEqual(1200, product.Sell_Price)
        self.assertEqual(80, product.Rent_Price)
        self.assertEqual(10, product.Stock)
        self.assertEqual(False, product.Sponsor_Status)
        self.assertEqual("test type", product_description.Type)
        self.assertEqual("testrange", product_description.Age_Range)
        self.assertEqual("test brand", product_description.Brand)
        self.assertEqual("red", product_description.Colour)
        self.assertEqual(40, product_description.Speeds)
        self.assertEqual(302, response.status_code)

    def test_deActivateProduct(self):
        client = Client()
        client.login(email='test@test.com', password='test')
        product = Products.objects.get(Product_ID=1)
        self.assertEqual(True, product.Is_Available)
        response = client.post('/account/shop/deactivate/1', {})
        product = Products.objects.get(Product_ID=1)
        self.assertEqual(False, product.Is_Available)
        self.assertEqual(302, response.status_code)

    def test_activateProduct(self):
        client = Client()
        client.login(email='test@test.com', password='test')
        product = Products.objects.get(Product_ID=1)
        self.assertEqual(True, product.Is_Available)
        response = client.post('/account/shop/deactivate/1', {})
        product = Products.objects.get(Product_ID=1)
        self.assertEqual(False, product.Is_Available)
        self.assertEqual(302, response.status_code)
        response = client.post('/account/shop/activate/1', {})
        product = Products.objects.get(Product_ID=1)
        self.assertEqual(True, product.Is_Available)
        self.assertEqual(302, response.status_code)

    #Test login has shop -  setup shop
    def test_exist_shop_setup_request(self):
        client = Client()
        client.login(email='test@test.com', password='test')
        response = client.get("/account/shopsetup/")
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed('Account/shopsetup.html')

    #Test login has no shop -  setup shop
    def test_shop_setup_request(self):
        client = Client()
        NewUser.objects.create_superuser(email='Noshop@test.com', password='Noshop')
        client.login(email='Noshop@test.com', password='Noshop')
        response = client.get("/account/shopsetup/")
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed('Account/shopsetup.html')

    #Test setup alt view should redirect
    def test_alt_shop_setup_request(self):
        client = Client()
        client.login(email='test@test.com', password='test')
        response = client.get("/account/setupshop/")
        self.assertEqual(302, response.status_code)
    
    #Test setup shop successful no images
    def test_shop_setup_success(self):
        client = Client()
        NewUser.objects.create_superuser(email='Noshop@test.com', password='Noshop')
        client.login(email='Noshop@test.com', password='Noshop')
        self.assertEqual(1, Shop.objects.count())
        response = client.post('/account/setupshop/',
                               {"header_img":"","logo":"","phone": "0432797899", "email": "Fakeemail@gmail.com", "location": "Test Location 123",
                                "url": "www.testshop.com","shop_name": "Test Shop","description": "desc","abn": 79000587780,"detail-confirm":True})
        shop = Shop.objects.get(ABN=79000587780)
        self.assertEqual(2, Shop.objects.count())
        self.assertEqual("0432797899", shop.Business_Number)
        self.assertEqual("Fakeemail@gmail.com", shop.Business_Email)
        self.assertEqual("Test Location 123", shop.Location)
        self.assertEqual("www.testshop.com", shop.Business_URL)
        self.assertEqual("Test Shop", shop.Business_Name)
        self.assertEqual("desc", shop.Description)
        self.assertEqual("", shop.Banner_URL)
        self.assertEqual("", shop.Logo_URL)
        self.assertEqual(79000587780, shop.ABN)

    #Test setup page accessed by guest
    def test_alt_shop_setup_request(self):
        client = Client()
        response = client.get("/account/setupshop/")
        #should redirect to login page
        self.assertEqual(302, response.status_code)

    def test_social_login_request(self):
        client = Client()
        response = client.get("/account/social-auth/login/facebook")
        #should redirect to facebook login page
        self.assertEqual(301, response.status_code)


        



    
