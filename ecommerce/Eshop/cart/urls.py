"""
URL configuration for Eshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from cart import views
app_name="cart"

from django.conf.urls.static import static

urlpatterns = [
   path('add-cart/<int:p>',views.add_cart,name="add_cart"),
   path('cart/',views.cartview,name='cartview'),
   path('orderform/',views.orderform,name='orderform'),
   path('cart-remove/<int:p>',views.cart_remove,name="cart_remove"),
   path('delete-cart/<int:p>',views.delete_cart,name="delete_cart"),
   path('orderview/',views.orderview,name="orderview"),

]
