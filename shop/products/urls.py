from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowProducts.as_view(), name='home'),
    path('about/<int:pk>', views.AboutProduct.as_view(), name='about'),
    path('cart/', views.CartDetail.as_view(), name='cart'),
    path('<int:pk>/', views.addToCart, name='add_to_cart'),
    # path('checkout/', views.total_price, name='checkout'),
]
