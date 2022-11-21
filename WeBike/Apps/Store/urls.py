from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='homepage'),
    path('about/', views.about_us, name='about_us'),
    path('cart/', views.cart_page, name='cart_page'),
    path('contactus/', views.contact_view, name='contact_us'),
    path('payment/', views.paymentpage, name='paymentpage'),
    path('payment/remove/<cart_id>', views.delete_cart, name='remove_cart'),
    path('productinfo/<product_id>/', views.product_info, name='product_info'),
    path('buy/<str:id>', views.cart_buy, name='cart_buy'),
    path('rent/<str:id>', views.cart_rent, name='cart_rent'),
    path('product/', views.productpage, name='productpage'),
    path('blog/', views.blog_page, name='blog_page'),
    # path for adding blog POST method
    path('postBlog/', views.postBlog, name='postBlog'),
    # path for removing blog POST method
    path('postBlogRemove/', views.postBlogRemove, name='postBlogRemove'),
    # path for adding self written blog POST method
    path('postSelfBlogAdd/', views.postSelfBlogAdd, name='postSelfBlogAdd'),
    path('successfullyPaid/', views.successfullyPaid, name='successfullyPaid'),
    path('cardpage/', views.card_page, name='cardpage'),
]
