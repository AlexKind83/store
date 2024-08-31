from django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('cart_add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart_change/', views.cart_change, name='cart_change'),
    path('cart_remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]
