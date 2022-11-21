from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    # path('login/', views.LoginView.as_view(), name="login"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('forgot/', views.ForgotPasswordView.as_view(), name="forgot"),
    path('success/', views.SuccessUserCreationView.as_view(), name="success"),
    path('shop/', views.shoppage, name='shoppage'),
    path('shop/edit', views.shop_submit_info, name="editshopprofile"),
    path('shop/editproduct/<str:id>', views.product_submit_info, name="editshopproduct"),
    path('shop/addproduct', views.add_product_info, name="addproduct"),
    path('shop/deactivate/<str:id>', views.deactivate, name='deactivate'),
    path('shop/activate/<str:id>', views.activate, name='activate'),
    path('profile/', views.userpage, name='userpage'),
    path('profile/edit', views.submit_info, name='editprofile'),
    path('orderHistory/', views.orderHistory, name='orderHistory'),
    path('shopsetup/', views.shopsetup, name='shopsetup'),
    # path for shop setup POST method
    path('setupshop/', views.setupshop, name='setupshop'),
    # path for review POST method
    path('postReview/', views.postReview, name='postReview'),
    path('social-auth/', include('social_django.urls', namespace="social")),
]
